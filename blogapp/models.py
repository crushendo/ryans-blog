from django.db import models

# Create your models here.

class Summaries(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(null=True)
    author = models.CharField(max_length=255, blank=True)
    keywords = models.TextField(blank=True)
    blurb = models.TextField(blank=True)
    content = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    slug = models.SlugField(unique=True)
