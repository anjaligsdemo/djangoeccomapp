from .models import Cart, CartItem
from .views import _cart_id


def cart_item_counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for each in cart_items:
                item_count += each.item_quantity
        except Cart.DoseNotExist:
            item_count = 0
    return dict(item_count=item_count)
