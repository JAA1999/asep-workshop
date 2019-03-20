from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import django.dispatch

from RNG.models import Rating, Game, Comment

# signals/receivers

# Check if when a user enter's a rating, they have made a comment
@receiver(pre_save)
def user_has_comment(sender, instance, **kwargs):
    comment = Comment.objects.get(user=instance.user, game=instance.game)
    if comment.exists():
        comment.rating = instance

# Check if when a user enter's a comment, if they have made a rating
@receiver(pre_save)
def user_has_rating(sender, instance, **kwargs):
    rating = Rating.objects.get(user=instance.user, game=instance.game)
    if rating.exists():
        instance.rating = rating


# readjust the fields of the Game object when a rating is deleted
@receiver(pre_delete)
def rating_deleted(sender, instance, **kwargs):
    # Get this rating's score
    score = instance.score

    # Get the new values for the Game's fields
    def update_values(cur_rating, num_rating):
        new_num_rating = num_rating - 1
        new_rating = ((cur_rating * num_rating) - score) / new_num_rating
        return new_rating, new_num_rating

    # Apply to correct rating type
    if instance.critic_rating:
        cur_rating = instance.game.avg_critic_rating
        num_rating = instance.game.num_critic_ratings
        cur_rating, num_rating = update_values(cur_rating, num_rating)
        instance.game.avg_critic_rating = cur_rating
        instance.game.num_critic_ratings = num_rating
    else:
        cur_rating = instance.game.avg_user_rating
        num_rating = instance.game.num_user_ratings
        cur_rating, num_rating = update_values(cur_rating, num_rating)
        instance.game.avg_user_rating = cur_rating
        instance.game.num_user_ratings = num_rating


pre_delete.connect(rating_deleted, sender=Rating)
pre_save.connect(user_has_comment, sender=Comment)
pre_save.connect(user_has_rating, sender=Rating)
