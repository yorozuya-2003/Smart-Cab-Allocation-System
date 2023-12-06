from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import User

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs.update({'placeholder': 'email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'password'})

        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''


class EmailUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    email = forms.EmailField(required=True,
        widget=forms.TextInput(attrs={'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['password1'].widget.attrs.update({'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'confirm password'})

