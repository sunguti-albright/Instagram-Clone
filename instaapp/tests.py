from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comment

# Create your tests here.
class ProfileClassTest(TestCase):
    def setUp(self):
        self.new_user = User(username='albright', email='albright@gmail.com', password='travisasutsa01')
        self.new_profile = Profile(profile_photo='', bio='albright.human', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
class ImageClassTest(TestCase):
    def setUp(self):
        self.new_user = User(username='albright', email='albright@gmail.com', password='travisasutsa01')
        self.new_image = Image( gallery_image='',image_name='Yoga', image_caption='Yoga is love', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        image = Image.objects.all()
        self.assertTrue(len(image)>0)
