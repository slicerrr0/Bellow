'''Custom form field validators.'''

import re
from typing import Collection
from django.core.exceptions import ValidationError
from django.core.validators import _ErrorMessage, EmailValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class UsernameOrEmailValidator(EmailValidator):
    '''Checks if the value is a valid username or email.'''
    username_regex = '[a-zA-Z0-9_]+'
    def __call__(self, value: str | None) -> None:
        # If value is not formatted as an email, verify it as a username first
        if not '@' in value and re.search(self.username_regex, value) is not None:
            return None
        elif not '@' in value:
            raise ValidationError(
                _('%(value)s contains illegal username characters.'),
                params={'value': value}
            )
        return super().__call__(value)