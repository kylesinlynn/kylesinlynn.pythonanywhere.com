from django.db import models

class Profile(models.Model):
    title = models.CharField(name='title', max_length=255, help_text='Enter your website title', null=True)
    description = models.TextField(name='description', max_length=500, help_text='Enter your website description', null=True)
    image = models.ImageField(name='profile_image', upload_to='uploads/', help_text="Upload your profile image", blank=True, null=True)
    email = models.EmailField(name='email', max_length=255, help_text="Enter your email address", null=True)
    phone = models.CharField(name='phone', max_length=255, help_text="Enter your phone number", null=True)
    facebook = models.CharField(name='facebook_username', max_length=255, help_text="Enter your facebook username", null=True)
    x = models.CharField(name='x_username', max_length=255, help_text="Enter your X username", null=True)
    github = models.CharField(name='github_username', max_length=255, help_text="Enter your GitHub username", null=True)