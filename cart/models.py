from django.db import models
from shops.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    cart_created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ('cart_created_date',)
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return str(self.cart_id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    cart_item_is_active = models.BooleanField(default=True)
    cart_item_created = models.DateField(auto_now_add=True)
    cart_item_updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'CartItem'
        ordering = ('cart_item_created',)
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def itemtotal(self):
        return self.product.pro_price * self.item_quantity

    def __str__(self):
        return str(self.product)

