from django.db import models
from django.utils import timezone
import uuid

from django.template.defaultfilters import slugify

# New AbstractBaseUser extension
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save  # try to implement post_save to update ratings
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save


# Database Objects
# Remember to migrate!
# Use python manage.py migrate --run-syncdb

# ID refs should autogenerate

class UserProfile(AbstractUser):
    # AbstractUser relevant fields:
    # username, password, first_name, last_name, date_joined, email, last_login
    critic = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=64)
    supercategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)

    avg_user_rating = models.FloatField(default=0)
    num_user_ratings = models.IntegerField(default=0)
    avg_critic_rating = models.FloatField(default=0)
    num_critic_ratings = models.IntegerField(default=0)

    age_rating = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    releasedate = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #images blank atm for testing
    #picture = models.ImageField(upload_to='game_images',blank=True)

    slug = models.SlugField(max_length=40, default=id)

    # def __init__(self):


    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.FloatField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    critic_rating = models.BooleanField()   # optional
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        def add_rating(self, cur_rating, num_ratings):
            new_num_ratings = num_ratings + 1
            new_rating = ((cur_rating * num_ratings) + self.score) / new_num_ratings
            return new_rating, new_num_ratings

        if self.critic_rating:
            cur_rating = self.game.avg_critic_rating
            num_ratings = self.game.num_critic_ratings
            cur_rating, num_ratings = add_rating(self, cur_rating, num_ratings)
            self.game.avg_critic_rating = cur_rating
            self.game.num_critic_ratings = num_ratings
        else:
            cur_rating = self.game.avg_user_rating
            num_ratings = self.game.num_user_ratings
            cur_rating, num_ratings = add_rating(self, cur_rating, num_ratings)
            self.game.avg_user_rating = cur_rating
            self.game.num_user_ratings = num_ratings

        super(Rating, self).save(*args, **kwargs)   # might go at end to exec code after saved


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    supercomment = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.game.name, str(self.user.username))


import RNG.signals