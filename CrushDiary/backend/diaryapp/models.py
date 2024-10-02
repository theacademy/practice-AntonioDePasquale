from django.db import models
from django.db.models import F ############

# Create your models here.
class SignInDetail(models.Model):
    email = models.EmailField(unique=True)
    password = models.TextField() 
    def __str__(self):
        return self.email

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    eyeColour = models.CharField(max_length=10)
    hairColour = models.CharField(max_length=20)
    # age = models.IntegerField()
    # fashionStyle = models.CharField(max_length=20)
    # crushName =models.CharField(max_length=30)
    email = models.OneToOneField(SignInDetail, on_delete=models.CASCADE)  
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method
        # Create a diary for the user
        Diary.objects.get_or_create(userId=self)  # Automatically create a diary linked to this user


class Diary(models.Model):
    diaryId = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)  
    # crush = models.CharField(max_length=100)
    # SELECT count(entryID) FROM User u LEFT JOIN Diary d ON u.userID=d.userID, LEFT JOIN Entry e ON d.diaryID=e.diaryID 
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def noOfEntries(self):
        return self.entries.count()

    # def __str__(self):
    #     return self.author  # or any other relevant field

    def save(self, *args, **kwargs):
        # Set the author field to the associated user's username
        if self.userId:
            self.author = self.userId.username
        super().save(*args, **kwargs)  # Call the original save method

    
    def __str__(self):
        return f"{self.author}'s Diary"  # Optional: can show username for clarity

class Crush(models.Model):
    crushId = models.AutoField(primary_key=True)
    crushName = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    matchingMoodEntries = models.IntegerField(default=0)  #increments with every matching entry mood,  matchingMoodEntries%3==0 triggers memo sent
    #crushPicture = picture = models.ImageField()
    # diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='crushes')  #################################


    def __str__(self): #################################################################
        return self.crushName

class Locker(models.Model):
    lockerId = models.AutoField(primary_key=True)
    diaryID = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='diary')
    # memo = models.CharField(max_length=500)


class Entry(models.Model):
    MOOD_CHOICES = [   #####################################
        ('Musical', 'Musical'),
        ('Sporty', 'Sporty'),
        ('Artistic', 'Artistic'),
        ('Fashion', 'Fashion'),
        ('Nerdy', 'Nerdy'),
    ]
    entryId = models.AutoField(primary_key=True)
    diaryId = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=100, choices=MOOD_CHOICES) #################
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        matching_crushes = Crush.objects.filter(mood=self.mood)
        for crush in matching_crushes:
            crush.matchingMoodEntries += 1
            crush.save()

            if (crush.matchingMoodEntries)%3==0: #################################
                self.create_memo(crush)
    def create_memo(self, crush):  #################################
        # Generate a title and content for the memo based on the number of matchingMoodEntries
        
        diary = self.diaryId

        try:
            locker = Locker.objects.get(diaryID=self.diaryId)
        except Locker.DoesNotExist:
        # If no locker exists for this diary, handle it (you might want to create one, raise an error, etc.)
            locker = Locker.objects.create(diaryID=self.diaryId)
        
        crushes = Crush.objects.filter(mood=self.mood)

        for crush in crushes:    
            title = None  
            content = None  
            if crush.matchingMoodEntries == 3:
                title = f"A Little Compliment from {crush.crushName}"
                content = f"Hey {self.diaryId.author},\n\nI couldn't help but notice how amazing your {self.diaryId.userId.eyeColour} eyes and {self.diaryId.userId.hairColour} hair look today. Honestly, you have this vibe that’s hard to ignore. Talk soon?\n\n- {crush.crushName}"
            elif crush.matchingMoodEntries == 6:
                if crush.mood == 'Sporty':
                    title = f"An Invite from {crush.crushName}"
                    content = f"Hey {self.diaryId.author},\n\nSo, I have a game coming up, and it'd be cool if you came to watch! I mean, no pressure, but it'd mean a lot to see you there cheering. Maybe we can hang out after?\n\nCatch you later,\n{crush.crushName}"
                elif crush.mood == 'Musical':
                    title = f"Come See My Band Play!"
                    content = f"Hey {self.diaryId.author},\n\nGuess what? My band is performing this weekend, and it’d be awesome if you could come. We’ve been practicing like crazy, and seeing you in the crowd would make it even better. What do you say?\n{crush.crushName}"
                elif crush.mood == 'Artistic':
                    title = f"Art Show Invitation from {crush.crushName}"
                    content = f"Hey {self.diaryId.author},\n\nI’ve got an art show coming up at school, and it’d be amazing if you could check it out. I’ve been working on some cool stuff and would love to hear what you think. Let’s hang out after?\n\n- {crush.crushName}"
                elif crush.mood == 'Fashion':
                    title = f"Fashion Show Invite!"
                    content = f"Hey {self.diaryId.author},\n\nWe’re doing this charity fashion show at school, and I’m walking in it. Would be awesome if you came to watch! Maybe you could tell me what you think of my outfits?\n\nSee you there,\n{crush.crushName}"
                elif crush.mood == 'Nerdy':
                    title = f"Meet Me at the Tree!"
                    content = f"Hey {self.diaryId.author},\n\nSo, I left a book in your locker. I thought you might like it. How about we meet by the big tree in the school park and read it together? It’s kinda my favorite, and I’d love to share it with you.\n\nSee you there?\n{crush.crushName}"
            elif crush.matchingMoodEntries == 9:
                title = f"A Question from {crush.crushName}"
                content = (
                    f"Dear {self.diaryId.author},\n\n"
                    f"Roses are red, violets are blue,\n"
                    f"I've had a secret I’ve been meaning to tell you.\n\n"
                    f"Your smile’s like the sunshine, your laugh’s like a song,\n"
                    f"I’ve felt this way for a while, maybe all along.\n\n"
                    f"So here’s the question, I’m hoping you’ll say yes,\n"
                    f"Would you be my date to prom? I think you’d look the best.\n\n"
                    f"Yours truly,\n{crush.crushName}"
                )
        

        # Create a new memo
        if title and content:
            Memo.objects.create(   #################################
                locker=locker,
                title=title,
                content=content
            )

        # Link the memo to the user's locker
        # Assuming each user has one locker
        # locker = Locker.objects.get(diaryID=self.diaryId)
        # locker.memo_set.add(Memo.objects.latest('id')) 
        
    def delete(self, *args, **kwargs):
        # No need to update diary here as noOfEntries is dynamic
        matching_crushes = Crush.objects.filter(mood=self.mood)
        for crush in matching_crushes:
            crush.matchingMoodEntries -= 1
            crush.save()

        super().delete(*args, **kwargs)

class Memo(models.Model):
    memoId = models.AutoField(primary_key=True)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name='memos')  #####################################
    title = models.CharField(max_length=500)
    content = models.TextField()
    #picture = models.ImageField()

    def __str__(self):  #################################
        return self.title
