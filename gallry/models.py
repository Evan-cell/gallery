
import datetime as dt
from django.db import models
from cloudinary.models import CloudinaryField

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')


    # description = models.TextField()
    # location = models.CharField(max_length=10)
    # created_at = models.DateTimeField(auto_now_add=True)