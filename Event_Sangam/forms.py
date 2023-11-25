from django import forms
from django.forms import ModelForm
#from .models import Profile, Contact


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password'
    }))
class Profile(ModelForm):
    class Meta:
        model = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'movie'
    }))
        fields = '__all__'
	#name = forms.CharField(required = True, max_length = 20, help_text = 'Your IG user name.')