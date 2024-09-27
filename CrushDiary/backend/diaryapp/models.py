from django.db import models

# Create your models here.
class SignInDetails(models.Model):
    email = models.EmailField(unique=True)
    password = models.TextField() 

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    # eyeColour = models.CharField(max_length=10)
    # hairColour = models.CharField(max_length=20)
    # age = models.IntegerField()
    # fashionStyle = models.CharField(max_length=20)
    # crushName =models.CharField(max_length=30)
    email = models.ForeignKey(SignInDetails, on_delete=models.CASCADE)

class Diary(models.Model):
    diaryId = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    crush = models.CharField(max_length=100)
    noOfEntries = models.IntegerField(default=0)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Entry(models.Model):
    entryId = models.AutoField(primary_key=True)
    diaryId = models.ForeignKey(Diary, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.TextField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    