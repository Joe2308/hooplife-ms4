from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):

    choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=choices, default=1)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default='')

    def __str__(self):
        return self.title
