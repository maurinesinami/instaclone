from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'insta/', blank = True)
    bio=models.CharField(max_length=50)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='insta/' )
    image_name = models.CharField(max_length=30)
    image_caption = HTMLField()
    
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)
    def __str__(self):
        return self.image_name
    @classmethod
    def images_all(cls):
        images = Image.objects.all()
        return images

    '''save function'''
    def save_post(self):
        self.save()

    '''delete function'''
    def delete_post(self):
        self.delete()

    '''search by image_name'''
    @classmethod
    def search_by_image_name(cls, search_term):
        images = cls.objects.filter(image_name__icontains=search_term)
        return images
    class Meta:
        ordering=['-id']
