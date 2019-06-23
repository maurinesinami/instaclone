from .models import Image, Profile
from django import forms
class NewsProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['']      
