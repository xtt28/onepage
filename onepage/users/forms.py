from django_registration.forms import RegistrationForm
from .models import AppUser


class AppUserRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = AppUser
