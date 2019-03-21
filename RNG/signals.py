from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import django.dispatch

from RNG.models import Rating, Game, Comment

# signals/receivers

# add checks for whether a user has already made rating to edit that one
# checks on creation of comments/ratings if user is critic

# Check if when a user enter's a rating, they have made a comment
# instance = Rating
# @receiver(pre_save, sender=Rating)
# def user_has_comment(sender, instance, **kwargs):
#     try:
#         comment = Comment.objects.get(user=instance.user, game=instance.game)
#         comment.rating = instance
#         comment.save()
#     except Comment.DoesNotExist:
#         ...
#
# # Check if when a user enter's a comment, if they have made a rating
# # on create
# @receiver(pre_save, sender=Comment)
# def user_has_rating(sender, instance, **kwargs):
#     try:
#         rating = Rating.objects.get(user=instance.user, game=instance.game)
#         instance.rating = rating
#         instance.save()
#     except Rating.DoesNotExist:
#         ...


# readjust the fields of the Game object when a rating is deleted
# @receiver(pre_delete, sender=Rating)
# def rating_deleted(sender, instance, **kwargs):
#     # Get this rating's score
#     score = instance.score
#
#     # Get the new values for the Game's fields
#     def update_values(cur_rating, num_rating):
#         new_num_rating = num_rating - 1
#         new_rating = ((cur_rating * num_rating) - score) / new_num_rating
#         return new_rating, new_num_rating
#
#     # Apply to correct rating type
#     if instance.critic_rating:
#         cur_rating = instance.game.avg_critic_rating
#         num_rating = instance.game.num_critic_ratings
#         cur_rating, num_rating = update_values(cur_rating, num_rating)
#         instance.game.avg_critic_rating = cur_rating
#         instance.game.num_critic_ratings = num_rating
#     else:
#         cur_rating = instance.game.avg_user_rating
#         num_rating = instance.game.num_user_ratings
#         cur_rating, num_rating = update_values(cur_rating, num_rating)
#         instance.game.avg_user_rating = cur_rating
#         instance.game.num_user_ratings = num_rating
#     instance.save()

# set the critic_rating field of Rating according to the user
# # pre create
# @receiver(pre_save, sender=Rating)
# def set_critic_rating(sender, instance, **kwargs):
#     instance.critic_rating = instance.user.critic
#     instance.save()

# pre_delete.connect(rating_deleted, sender=Rating)
# pre_save.connect(user_has_comment, sender=Rating)
# pre_save.connect(user_has_rating, sender=Comment)
