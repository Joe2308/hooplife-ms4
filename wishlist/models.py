from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Wislist model based on slack research
class Wishlist(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, related_name='wishlist'
        )
    products = models.ManyToManyField(Product, through='WishlistItem')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
