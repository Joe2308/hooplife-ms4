from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import Add_ReviewForm
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from django.urls import reverse


def add_review(request, product_id):
    ''' View to add reviews '''
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = Add_ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
    form = Add_ReviewForm()
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'reviews/add_review.html', context)
