from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.AllCatPro, name='AllCatProduct'),
    path('<slug:cat_slug>/', views.AllCatPro, name='AllProductCat'),
    path('<slug:cat_slug>/<slug:pro_slug>', views.ProductDetails, name='ProductDetails')
    ]