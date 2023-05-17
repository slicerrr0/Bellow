'''Custom post validators.'''

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .choices import FlairColors

def flair_validator(value):
    '''Checks that `value` is in the list of selectable flair colors.'''
    if not value in FlairColors.colors.values():
        raise ValidationError(
            _('%(value)s is not a valid flair color.'),
            params={'value': value}
        )