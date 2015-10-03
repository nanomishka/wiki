from django.db import models

# Create your models here.

class Files(models.Model):
	name = models.CharField(max_length=40, unique=True, blank=False)
	data = models.TextField(default="")
	url = models.CharField(max_length=40, unique=True, blank=False)