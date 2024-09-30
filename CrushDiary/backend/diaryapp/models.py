from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    email = models.ForeignKey(SignInDetail, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Diary(models.Model):
    diaryId = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    # crush = models.CharField(max_length=100)
    # SELECT count(entryID) FROM User u LEFT JOIN Diary d ON u.userID=d.userID, LEFT JOIN Entry e ON d.diaryID=e.diaryID 
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def noOfEntries(self):
        return self.entries.count()

    def __str__(self):
        return self.author  # or any other relevant field
    
class Entry(models.Model):
    entryId = models.AutoField(primary_key=True)
    diaryId = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='entries')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Check if the entry's mood matches any crush's mood
        for crush in Crush.objects.all():  # All available NPCs (crushes)
            if crush.mood == self.mood:
                crush.increment_matching_mood_entries()

    def delete(self, *args, **kwargs):
        matching_crushes = Crush.objects.filter(mood=self.mood)
        for crush in matching_crushes:
            crush.matchingMoodEntries -= 1
            crush.save()

        super().delete(*args, **kwargs)

class Locker(models.Model):
    lockerId = models.AutoField(primary_key=True)
    diary = models.OneToOneField(Diary, on_delete=models.CASCADE, related_name='locker')
    # memo = models.CharField(max_length=500)

class Memo(models.Model):
    memoId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    #picture = models.ImageField()
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name='memos')

    def __str__(self):
        return self.title

class Crush(models.Model):
    crushId = models.AutoField(primary_key=True)
    crushName = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    matchingMoodEntries = models.IntegerField(default=0)  # increments with every matching entry mood

    # Define unique templates for each crush
    memo_templates = {
        'Dante': [
            "Hey {username}, I noticed your {hairColour} hair shining while listening to music!",
            "Your {eyeColour} eyes remind me of the melodies in my heart.",
            "You always make me think of {mood} songs!"
        ],
        'Tristan': [
            "Hey {username}, your {hairColour} hair looked amazing on the field today!",
            "Those {eyeColour} eyes sparkled with joy while playing!",
            "Your {mood} spirit makes every game exciting!"
        ],
        'Raphael': [
            "Hey {username}, your {hairColour} hair is like a canvas of creativity!",
            "Those {eyeColour} eyes inspire me to see beauty in art.",
            "Every brushstroke of your {mood} mood adds color to my day!"
        ],
        'Caspian': [
            "Hey {username}, your {hairColour} hair is always stylish!",
            "Your {eyeColour} eyes see the world through a fashion lens.",
            "Your {mood} vibe brings out the best in everyone!"
        ],
        'Sebastian': [
            "Hey {username}, your {hairColour} hair shows off your nerdy charm!",
            "Those {eyeColour} eyes are filled with curiosity!",
            "Your {mood} personality makes every conversation enjoyable!"
        ]
    }

    def increment_matching_mood_entries(self):
        self.matchingMoodEntries += 1
        self.save()

        # Check if the number of matching mood entries triggers a memo (3, 6, 9, etc.)
        if self.matchingMoodEntries in [3, 6, 9]:
            self.send_memo()

    def send_memo(self):
        """
        Sends a specific memo based on the crush mood and matchingMoodEntries value.
        """
        diaries = Diary.objects.all()  # Get all diaries
        for diary in diaries:
            locker = Locker.objects.get(diary=diary)

            # Get the appropriate memo template based on current matching mood entries
            templates = self.memo_templates.get(self.crushName, [])
            if not templates:
                return  # No templates found for this crush

            # Determine the template index based on matchingMoodEntries
            index = (self.matchingMoodEntries // 3) - 1  # 3 -> 0, 6 -> 1, 9 -> 2
            memo_content = templates[index].format(
                username=diary.userId.username,
                hairColour=diary.userId.hairColour,
                eyeColour=diary.userId.eyeColour,
                mood=self.mood
            )
            memo_title = f"{self.crushName} Memo {self.matchingMoodEntries // 3}"  # Determine the memo number
            
            # Create the memo
            Memo.objects.create(locker=locker, title=memo_title, content=memo_content)

    def __str__(self):
        return self.crushName



