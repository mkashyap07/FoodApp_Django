from django.db import models
from django.db import connections

# Create your models here.
class Order(models.Model):
    uname=models.CharField(max_length=122)
    date=models.DateField(null=True)
    email=models.CharField(max_length=122)
    number=models.BigIntegerField()
    food=models.CharField(max_length=122)
    Restaurant=models.CharField(max_length=122)
    drinks=models.CharField(max_length=122)
    soups=models.CharField(max_length=122)
    dish=models.CharField(max_length=122)
    order=models.CharField(max_length=122)

