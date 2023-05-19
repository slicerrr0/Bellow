from django.db import models
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from account.models import CustomUser
from community.models import Community
from .mixins import SubmissionMixin

# Create your models here.

class Flair(models.Model):
    '''Custom messages or descriptors for tagging posts.'''
    class FlairColor(models.TextChoices):
        NONE = None, _('None')
        RED = 'Red', _('Red')
        BLUE = 'Blue', _('Blue')
        GREEN = 'Green', _('Green')
        YELLOW = 'Yellow', _('Yellow')
        ORANGE = 'Orange', _('Orange')
        PURPLE = 'Purple', _('Purple')
        BROWN = 'Brown', _('Brown')
        BLACK = 'Black', _('Black')
    
    color = models.CharField(
        max_length=6, 
        help_text='Flair color.', 
        choices=FlairColor.choices,
        default=FlairColor.NONE, 
    )
    text = models.CharField(max_length=24, help_text='Flair message.')

class Post(models.Model, SubmissionMixin):
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL,
        null=True,
        help_text='User that made the post.',
        related_name='post_user'
    )
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, help_text='Date and time the post was created.')
    flair = models.ForeignKey(
        Flair, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE, 
        help_text='Optional post flair.'
    )
    message = models.TextField(max_length=1000, help_text='Post content.')
    upvotes = models.ManyToManyField(
        CustomUser, 
        help_text='Users who have upvoted this post.',
        related_name='post_upvoters'
    )
    downvotes = models.ManyToManyField(
        CustomUser, 
        help_text='Users who have downvoted this post.',
        related_name='post_downvoters'
    )
    fire_index = models.IntegerField(
        default=0, 
        help_text='Net change to score over the past day. Used to sort by "hotness".'
    )

class EmbeddedImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, help_text='Image embedded in post content.', validators=[validate_image_file_extension])
    image = models.ImageField()
    # https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/