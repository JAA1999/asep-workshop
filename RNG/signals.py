from django.contrib.auth.models import Rating
from django.db.models.signals import post_save, pre_delete
#from django.dispatch import receiver
import django.dispatch

@receiver(post_save, sender=Rating)
def save_rating(sender, instance, **kwargs):
    if not self.pk: # only executes if object not in db yet
        # recalc rating on game
        cur_score = Game.objects.get(game).avg_user_rating
        num_scores = game.num_user_ratings

    super(Rating, self).save(*args, **kwargs)

def delete_rating(sender, instance, **kwargs):
    score = instance.g

pre_delete.connect(delete_rating, sender=Rating)
