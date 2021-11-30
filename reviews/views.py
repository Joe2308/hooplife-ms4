from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import Add_ReviewForm
from django.contrib import messages
from products.models import Product
from django.urls import reverse


def reviews(request):
    ''' View to return review page '''
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review.html', context)


def add_review(request, product_id):
    ''' View to add reviews '''
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = Add_ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
    form = Add_ReviewForm()
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'reviews/add_review.html', context)
