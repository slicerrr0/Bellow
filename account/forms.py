from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class SignInForm(AuthenticationForm):
    pass

class RegistrationForm(UserCreationForm):
    pass
