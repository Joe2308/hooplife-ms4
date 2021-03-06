from django.shortcuts import (
    render, redirect, reverse, HttpResponseRedirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem


# Credit idea for wishlist https://youtu.be/OgA0TTKAtqQ
# Also based on slack research
@login_required()
def wishlist(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context=context)


@login_required()
def add_to_wishlist(request, product_id):
    """
    A view to add a product from the store to the user's
    wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if WishlistItem.objects.filter(
        wishlist=wishlist, product=product
    ).exists():
        messages.error(request, 'Product already in your wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist.products.add(product)
        messages.success(request, 'product added to wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))


@login_required()
def remove_from_wishlist(request, product_id):
    """
    A view to remove products from the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, 'product removed from wishlist')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
