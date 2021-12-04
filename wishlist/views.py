from django.shortcuts import render, get_object_or_404
from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem


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
