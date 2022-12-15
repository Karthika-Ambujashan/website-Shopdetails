from django.db import models

# Create your models here.
class Shopdb(models.Model):
    shopname=models.CharField(max_length=15)
    shoplocation=models.CharField(max_length=15)
    shopcontactno=models.IntegerField()
    shop_image=models.ImageField(upload_to='image',default="null.jpg")