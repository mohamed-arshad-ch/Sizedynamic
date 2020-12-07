from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    goo_uid = models.CharField(max_length=150)

    def __str__(self):
        return self.mobile_no


class PictureSize(models.Model):
    image = models.ImageField()
    width = models.IntegerField()
    height = models.IntegerField()
    widtininch = models.IntegerField()
    heightininch = models.IntegerField()
    size = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    strength = models.FloatField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


