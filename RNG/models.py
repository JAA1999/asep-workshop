from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


# Database Objects

#Sign up doesnt work with this class so I've commented it out for now and used 
#the defaul django user model for regualr users and changed this to a critic model
class Users(models.Model):
    # might use an ID integer as PK for more efficient sorting/searching
    username = models.CharField(max_length = 16, unique = True, primary_key = True)
    password = models.CharField(max_length = 32)
    email = models.EmailField(blank=True)     # make unique = true later
	
    # password      need to setup password hasher etc
    critic = models.BooleanField(default=False)
    website = models.URLField(blank=True)    # not sure if optional is a param or if it is just left null
    description = models.TextField(blank=True)
	
    def __str__(self):
         return self.username

    # might need list[fk] for ratings

class Game(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    name = models.CharField(max_length = 64)
    user_score = models.FloatField()
    num_user_ratings = models.IntegerField()
    critic_score = models.FloatField()
    num_critic_ratings = models.IntegerField()
    age_rating = models.CharField(max_length = 16)
    description = models.TextField()
    #need to add into pop script
    releasedate = models.DateField()

    # might need list[fk] for ratings
    def __str__(self):
        return self.title

class Rating(models.Model):
    ID = models.IntegerField(primary_key = True, unique = True)
    score = models.FloatField()
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    supercategory = models.ForeignKey('self', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
	
