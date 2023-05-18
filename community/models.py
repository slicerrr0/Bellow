from django.db import models

# Create your models here.

class Community:
    name = models.CharField(max_length=64, help_text='Name of the community.')
    private = models.BooleanField(default=False, help_text='Specifies if a community is invite-only.')
    member_only = models.BooleanField(default=False, help_text='Specifies if users must be a member to post.')
    allowed_groups = models.Choices
    description = models.TextField(max_length=300, blank=True, null=True, help_text='Community description.')