from django.db import models

class Image(model.Model):
    image = models.ImageField(upload_to ='insta/' )
    image_name = models.charField(max_length=30)
    image_caption = HTMLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)
    def __str__(self):
        return self.image_name