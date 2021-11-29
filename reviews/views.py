from django.shortcuts import render
from .models import Review
from .forms import Add_ReviewForm

# Create your views here.

def reviews(request):
    ''' View to return review page '''
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review.html', context)

def add_review(request):
    ''' View to return review page '''
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save
    form = Add_ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/add_review.html', context)
