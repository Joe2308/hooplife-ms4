from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
