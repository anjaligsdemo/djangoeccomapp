from django.shortcuts import render, redirect, get_object_or_404
from shops.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except ObjectDoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.item_quantity < cart_item.product.pro_stock:
            cart_item.item_quantity += 1
        cart_item.save()
    except ObjectDoesNotExist:
        cart_item = CartItem.objects.create(product=product, item_quantity=1, cart=cart)
        cart_item.save()
    return redirect('cart:cart_details')


def cart_details(request, itemtotal=0, item_count=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, cart_item_is_active=True)
        for each in cart_items:
            itemtotal += (each.product.pro_price * each.item_quantity)
            item_count += each.item_quantity

    except ObjectDoesNotExist:
        pass
    context= {'cart_products': cart_items,
              'item_total_amount': itemtotal,
              'item_count': item_count
              }
    return render(request, 'cartdetails.html', context)


def cart_remove_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.item_quantity > 1:
        cart_item.item_quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_details')


def cart_delete_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_details')