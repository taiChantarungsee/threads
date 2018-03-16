from django.db import models

class location(models.Model):
	laua_code = models.CharField(max_length=10)
	laua_name = models.CharField(max_length=10)
	average_download_speed = models.FloatField()

class district(models.Model):
	la_code = models.CharField(max_length=8)
	la_name = models.CharField(max_length=20)
	average_download_speed = models.FloatField()