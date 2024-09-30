from django.db import models

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
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=100)
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
        
    def delete(self, *args, **kwargs):
        # No need to update diary here as noOfEntries is dynamic
        matching_crushes = Crush.objects.filter(mood=self.mood)
        for crush in matching_crushes:
            crush.matchingMoodEntries -= 1
            crush.save()

        super().delete(*args, **kwargs)

class Locker(models.Model):
    lockerId = models.AutoField(primary_key=True)
    diaryID = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='diary')
    # memo = models.CharField(max_length=500)

class Memo(models.Model):
    memoId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    #picture = models.ImageField()

class Crush(models.Model):
    crushId = models.AutoField(primary_key=True)
    crushName = models.CharField(max_length=100)
    mood = models.CharField(max_length=100)
    matchingMoodEntries = models.IntegerField(default=0)  #increments with every matching entry mood,  matchingMoodEntries%3==0 triggers memo sent
    #crushPicture = picture = models.ImageField()
