from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .validators import UsernameOrEmailValidator

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        min_length=6,
        max_length=64,
        label=_('Username or email'),
        widget=forms.TextInput(attrs={'autofocus': True}),
        validators=[UsernameOrEmailValidator],
        strip=True,
        initial='username or email',
        required=True
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
        initial='password',
        required=True
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ()
