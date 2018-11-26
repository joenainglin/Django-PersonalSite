from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 250)
	slug = models.SlugField(unique=True)
	subject = models.CharField(max_length=250)
	body = models.CharField(max_length = 250)
	image = models.ImageField(upload_to='Posts/%Y/%m/%d/', blank=False)

	def __str__(self):
		return self.title
	

class Person(models.Model):
	title = models.CharField(max_length = 250)
	position = models.CharField(max_length=250)
	bio = models.CharField(max_length=250)
	image = models.ImageField(upload_to='Posts/%Y/%m/%d/', blank=False)

	def __str__(self):
		return self.title
	
		