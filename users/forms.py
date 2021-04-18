""" Users forms. """

# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Models
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """ Form for new users. """

    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        """ META class. """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """ Form to update useres data. """

    email = forms.EmailField()
    
    class Meta:
        """ META class. """

        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ Form to update useres data. """

    class Meta:
        """ META class. """
        
        model = Profile
        fields = ['image']