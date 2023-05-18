from django.db import models
from account.models import CustomUser
from community.models import Community
from post.mixins import SubmissionMixin

# Create your models here.

class Comment(models.Model, SubmissionMixin):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    message = models.TextField(max_length=200, help_text='Comment content.')
    score = models.IntegerField(default=0, help_text='Net sum of upvotes and downvotes this comment has received.')
    fire_index = models.IntegerField(default=0, help_text='Net change to score over the past day. Used to sort by "hotness".')