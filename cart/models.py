from django.db import models
from django.contrib.auth.models import User
from toy.models import Toy

class CartItem(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)