from django.db import models


class drinks(models.Model):
    name = models.CharField(max_length=255,unique=True)
    company = models.CharField(max_length=255)
    quantity = models.IntegerField(null=False)
    prize = models.FloatField(null=False)
    discount = models.IntegerField(null=True)

    def __str__(self):
        return self.name