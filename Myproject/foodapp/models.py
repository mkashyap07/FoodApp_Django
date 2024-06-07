from django.db import models
from django.db import connections
# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.ImageField(max_length=5000,default='https://as2.ftcdn.net/v2/jpg/02/88/85/71/1000_F_288857162_l7ZOOsEveQf1d8PMsNC6HMQFeqafLJhx.jpg')

    def __str__(self):
        return self.item_name
    
class Contact2(models.Model):
    name2=models.CharField(max_length=122)
    email2=models.CharField(max_length=122)
    phone2=models.CharField(max_length=12)