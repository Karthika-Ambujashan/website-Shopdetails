from django.db import models

# Create your models here.
class Userdb(models.Model):
    shop_image=models.ImageField(upload_to = 'image',default="null.jpg")