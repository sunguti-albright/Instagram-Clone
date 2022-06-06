from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from PIL import Image
import cloudinary
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    bio = models.TextField()
    profile_photo = CloudinaryField('profile_photo')


    def save_profile(self):
        self.save()
