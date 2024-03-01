from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()


