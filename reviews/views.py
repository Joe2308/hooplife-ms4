from django.shortcuts import render
from .models import Review

# Create your views here.

def reviews(request):
    ''' View to return review page '''
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review.html', context)
