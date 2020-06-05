from django.db import models

# Create your models here.
class Vlog(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	image = models.ImageField(upload_to='image/')