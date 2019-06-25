from .models import Image, Profile,Comment
from django import forms
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','comments']      
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image','user']     
