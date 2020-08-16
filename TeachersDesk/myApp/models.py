from django.db import models

from django.forms import ModelForm, Textarea
from django.db import models

class Students(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
class Meta:
    db_table= 'students'


class Lectures(models.Model):
	link = models.CharField(max_length=100)
	Time = models.TimeField()
	cid = models.CharField(max_length=100)
	tid = models.CharField(max_length=100)
class Meta:
	db_table= 'lectures'
