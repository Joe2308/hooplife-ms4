from django.shortcuts import render

# Create your views here.

def review(request):
    ''' View to return review page '''
    return render(request, 'reviews/review.html')
