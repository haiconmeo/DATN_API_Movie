from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):

    Name = models.CharField(max_length=70)

class Movie(models.Model):

    Movie = models.CharField(max_length=70)
    Categori = models.ManyToManyField(Category)
    Year = models.IntegerField()
    Content = models.TextField()
    Image = models.ImageField() 
    deleted =  models.BooleanField(default=False)


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fistname =  models.CharField(max_length=30, blank=True)
    lastname =  models.CharField(max_length=30, blank=True)
    phonenum = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    cmmd = models.CharField(max_length=30, blank=True)
    deleted =  models.BooleanField(default=False)

class Rate(models.Model):
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rate_u = models.IntegerField()


