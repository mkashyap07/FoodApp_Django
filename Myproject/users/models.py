from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user_instance=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_images',default='profile.jpg')

