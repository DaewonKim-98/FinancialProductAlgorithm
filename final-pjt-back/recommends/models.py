from django.db import models
from django.conf import settings


# Create your models here.
class AddInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deposit_money = models.IntegerField()
    saving_money = models.IntegerField()
    total_money = models.IntegerField()
    target_place = models.TextField()
    move_time = models.TextField()


class RealEstate(models.Model):
    sigu = models.CharField(max_length=255)
    average_price = models.IntegerField()
