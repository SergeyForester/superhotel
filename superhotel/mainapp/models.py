from django.db import models

# Create your models here.

class Table(models.Model):
	field = models.CharField( max_length=100)

class constructNameHotel(models.Model):
	tag_name = models.CharField(verbose_name='имя', max_length=64, unique=True)
	tag_text = models.TextField(verbose_name='описание', blank=True)

	def __str__(self):
		return self.tag_name
