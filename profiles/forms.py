from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from profiles.models import Profile


class ProfileCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(ProfileCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = Profile
        fields = ("email", "photo", "frontend", "backend", "year_started_learning", "company")


class ProfileChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(ProfileChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = Profile
        fields = "__all__"
