from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	image = models.ImageField(upload_to='image/')

	def __str__(self):
		return self.title