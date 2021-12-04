from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404
from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem
from django.contrib import messages


def wishlist(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        wishlist = Wishlist.objects.get(user=profile)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context=context)


def add_to_wishlist(request, product_id):
    """
    A view to a product from the store to the user's
    wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    wishlist, created = Wishlist.objects.get_or_create(user=profile)

    if WishlistItem.objects.filter(product=product).exists():
        messages.error(request,'Product already in your wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist.products.add(product)
        messages.success(request, 'product added to wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
