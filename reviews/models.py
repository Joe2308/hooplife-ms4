from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default='')

    def __str__(self):
        return self.title
