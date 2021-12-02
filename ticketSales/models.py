from django.db import models

# Create your models here.

class concertModel(models.Model):
  Name=models.CharField(max_length=100)
  SingerName=models.CharField(max_length=100)
  length=models.IntegerField()

  def __str__(self):
    return self.SingerName

class locationModel(models.Model):
  Name=models.CharField(max_length=100)
  Address=models.CharField(max_length=500)
  Phone=models.CharField(max_length=11)
  capacity=models.IntegerField()

  def __str__(self):
    return self.Name