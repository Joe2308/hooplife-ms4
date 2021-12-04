from django.urls import path
from . import views

urlpatterns = [
    path('my_wishlist/', views.wishlist, name='wishlist'),
]