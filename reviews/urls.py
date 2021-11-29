from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.reviews, name='reviews'),
    path('add/', views.add_review, name='add_review'),
]