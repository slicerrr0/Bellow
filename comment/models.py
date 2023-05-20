from django.db import models
from django.utils import timezone
from account.models import CustomUser
from community.models import Community
from post.mixins import SubmissionMixin

# Create your models here.

class Comment(models.Model, SubmissionMixin):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=None, related_name='comment_user')
    created_at = models.DateTimeField(
        default=timezone.now, 
        help_text='Time and date this comment was created.'
    )
    parent = models.ForeignKey("Comment", on_delete=models.SET_DEFAULT, default=None)  # Recursive relationship
    message = models.TextField(max_length=200, help_text='Comment content.')
    upvotes = models.ManyToManyField(
        CustomUser, 
        help_text='Users who have upvoted this comment.',
        related_name='comment_upvoters'
    )
    downvotes = models.ManyToManyField(
        CustomUser, 
        help_text='Users who have downvoted this comment.',
        related_name='comment_downvoters'
    )
    fire_index = models.IntegerField(
        default=0, 
        help_text='Net change to score over the past day. Used to sort by "hotness".'
    )