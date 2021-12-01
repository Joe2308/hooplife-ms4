from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'body',
        'product',
        'user',
        'date'
    )

    ordering = ('product', )

admin.site.register(Review, ReviewAdmin)
