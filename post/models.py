from django.db import models
from django.core.validators import validate_image_file_extension
from account.models import CustomUser
from .choices import FlairColors
from .validators import flair_validator

# Create your models here.

class Flair(models.Model):
    '''Custom messages or descriptors for tagging posts.'''
    color = models.CharField(max_length=6, help_text='Flair color.', choices=FlairColors.create_choices(), validators=[flair_validator])
    text = models.CharField(max_length=24, help_text='Flair message.')

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, help_text='User that made the post.')
    created_at = models.DateTimeField(help_text='Date and time the post was created.')
    flair = models.ForeignKey(Flair, blank=True, null=True, on_delete=models.PROTECT, help_text='Optional post flair.')
    message = models.TextField(max_length=1000, help_text='Post content.')

class EmbeddedImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, help_text='Image embedded in post content.', validators=[validate_image_file_extension])
    image = models.ImageField()
    # https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/