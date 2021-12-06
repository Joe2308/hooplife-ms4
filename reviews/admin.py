from django.contrib import admin
from .models import Review


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
