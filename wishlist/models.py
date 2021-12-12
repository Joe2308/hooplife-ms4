from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Wislist model based on slack research
class Wishlist(models.Model):
    user = models.OneToOneField(
        User, null=False, blank=False,
        on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(
        Product, default="", through='WishlistItem')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False, on_delete=models.CASCADE,
        related_name='wishlist_items')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE,
        related_name='wishlist_products')

    def __str__(self):
        return self.product.name
