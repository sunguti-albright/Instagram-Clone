# Generated by Django 3.1.2 on 2022-06-06 16:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='gallery_image')),
                ('image_name', models.CharField(max_length=30, null=True)),
                ('image_caption', models.CharField(max_length=70, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('liked', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='instaapp.profile')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]