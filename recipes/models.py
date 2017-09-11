from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class RecipePost(models.Model):
	
	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.jpg', verbose_name='foodphoto')
	prep_time = models.CharField(max_length=15)
	cooking_time = models.CharField(max_length=15)
	servings = models.CharField(max_length=15)
	ingridients = models.CharField(max_length=100)
	cooking_instaructions = RichTextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "posts/get/%i/" % self.id

