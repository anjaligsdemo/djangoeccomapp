from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_details, name='cart_details'),
    path('remove-item/<int:product_id>/', views.cart_remove_item, name='cart_remove_item'),
    path('delete-item/<int:product_id>/', views.cart_delete_item, name='cart_delete_item'),
    ]