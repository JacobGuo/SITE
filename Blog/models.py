from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	subTitle = models.CharField(max_length=200)
	tag = models.CharField(max_length=200)
	content = models.CharField(max_length=20000)
	pageID = models.CharField(max_length=10,default='001');
	def __unicode__(self):
		return self.title