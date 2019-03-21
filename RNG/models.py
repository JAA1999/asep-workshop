from django.db import models
from django.db.models import Avg
from django.utils import timezone
import uuid

from django.template.defaultfilters import slugify

# New AbstractBaseUser extension
from django.contrib.auth.models import AbstractUser

# Database Objects
# Remember to migrate!
# Use python manage.py migrate --run-syncdb

# ID, slug refs should autogenerate

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
    ### IMPORTANT ###
    # averages should not be fields but instead use aggregation
    # use django's annotate()
    # https://docs.djangoproject.com/en/2.0/topics/db/aggregation/
    # https://stackoverflow.com/questions/48792847/django-model-field-auto-updates-depending-on-related-instances

    name = models.CharField(max_length=64)

    age_rating = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #images blank atm for testing
    #picture = models.ImageField(upload_to='game_images',blank=True)

    slug = models.SlugField(max_length=40)

    @property
    def avg_user_rating(self):
        return Rating.objects.filter(game='self', critic_rating=False).aggregate(Avg('score'))

    @property
    def avg_critic_rating(self):
        return Rating.objects.filter(game='self', critic_rating=True).aggregate(Avg('score'))

    def avg_rating(self):
        return Rating.objects.filter(game='self').aggregate(Avg('score'))

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    score = models.FloatField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    critic_rating = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def clean(self):
        #print("Rating clean: User[" + str(self.user) + "] + critic_rating[" + str(self.critic_rating) + "]")
        if self.user:
            self.critic_rating = self.user.critic   # auto set critic rating by user


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True, blank=True)

    content = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    supercomment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        # auto get user's rating for game where comment is made
        if not self.rating:
            try:
                self.rating = Rating.objects.get(user=self.user, game=self.game)
            except Rating.DoesNotExist:
                ...

    def __str__(self):
        return '{} - {}'.format(self.game.name, str(self.user.username))

#import RNG.signals