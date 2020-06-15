from django.db import models
from datetime import date
# Create your models here.

class User(models.Model):
    username = models.CharField('User name', max_length=100)
    email = models.CharField('User email', max_length=100)
    password = models.CharField('User Password', max_length=20)

    def __str__(self):
        return self.username

class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Post Title', max_length=100)
    description = models.TextField('Post Description')
    posted_date = models.DateField(default=date.today)
    good_name = models.CharField('Good Name', max_length=100)

    def __str__(self):
        return self.title