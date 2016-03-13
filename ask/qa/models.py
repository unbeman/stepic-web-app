# coding: utf-8
import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models.User import AbstractUser

# Create your models here.
class User(AbstractUser):
	

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(Likes)

	def __unicode__(self):
		return self.title

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.text
