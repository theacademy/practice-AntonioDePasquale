from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure the email is unique

    def __str__(self):
        return self.email  # Display email in admin

# Get the user model
User = get_user_model()  # This will return your custom user model

class PlayerCharacter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Use User here instead of the default User
    inGameName = models.CharField(max_length=30)
    eyeColour = models.CharField(max_length=10)
    hairColour = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the original save method
        # Comment out the diary and locker creation to avoid issues during user registration
        # diary, created = Diary.objects.get_or_create(playerCharacterId=self, author=self.inGameName)
        # if created:
        #     Locker.objects.create(diaryId=diary)  # Create a locker associated with the diary


class Diary(models.Model):
    diaryId = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)  
    playerCharacterId = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name='diaries')

    # def save(self, *args, **kwargs):
    #     # Set the author field to the associated user's username
    #     if self.playerCharacterId:
    #         self.author = self.playerCharacterId.user
    #     super().save(*args, **kwargs)  # Call the original save method

    @property
    def noOfEntries(self):
        return self.entries.count()

    def __str__(self):
        return f"{self.author}'s Diary"  # Optional: can show username for clarity

class Crush(models.Model):
    crushId = models.AutoField(primary_key=True)
    crushName = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    matchingMoodEntries = models.IntegerField(default=0)

    def __str__(self):
        return self.crushName

class Locker(models.Model):
    lockerId = models.AutoField(primary_key=True)
    diaryId = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='lockers')

    def __str__(self):
        return f"Locker for {self.diaryId.author} (Diary ID: {self.diaryId.diaryId})"

class Entry(models.Model):
    MOOD_CHOICES = [
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
    mood = models.CharField(max_length=100, choices=MOOD_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        matchingCrushes = Crush.objects.filter(mood=self.mood)
        for crush in matchingCrushes:
            crush.matchingMoodEntries += 1
            crush.save()

            if (crush.matchingMoodEntries) % 3 == 0:
                self.createMemo(crush)

    def createMemo(self, crush):
        diary = self.diaryId

        try:
            locker = Locker.objects.get(diaryId=self.diaryId)
        except Locker.DoesNotExist:
            locker = Locker.objects.create(diaryId=self.diaryId)

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
            Memo.objects.create(
                locker=locker,
                title=title,
                content=content
            )

    def delete(self, *args, **kwargs):
        matchingCrushes = Crush.objects.filter(mood=self.mood)
        for crush in matchingCrushes:
            crush.matchingMoodEntries -= 1
            crush.save()

        super().delete(*args, **kwargs)

class Memo(models.Model):
    memoId = models.AutoField(primary_key=True)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name='memos')
    title = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.title


