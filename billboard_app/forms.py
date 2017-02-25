from django.contrib.auth.models import User
from django import forms
from .models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'author')
        labels = {
            'title': "",
            'text': "",
            'author': "",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-input', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'text-input', 'placeholder': 'Enter message here'}),
            'author': forms.TextInput(attrs={'class': 'author-input', 'placeholder': 'Author'}),
        }



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')