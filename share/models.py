from django.db import models

from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

class RichText(models.Model):

    content=RichTextField(blank=True, null=True)
    content_images=RichTextUploadingField(blank=True,null=True)
    content_link=models.CharField(max_length=200,default=" ")

class User_Save(models.Model):
    user_content = models.ForeignKey(User, on_delete=models.CASCADE)
    user_content_link=models.CharField(max_length=100,default=" ")
    owner=models.CharField(max_length=100,default=" ")

