import datetime

from django.db import models

# Create your models here.

class SearchQuery(models.Model):
	query = models.CharField(max_length=100)
	formatted_name = models.CharField(max_length=200, default='')
	search_time = models.DateTimeField('time searched')

	def __str__(self):
		return self.query