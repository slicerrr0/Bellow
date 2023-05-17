from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class SignInForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = [

        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            
        ]
