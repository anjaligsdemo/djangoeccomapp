from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def homepage(request):
    return render(request, 'base.html')


def AllCatPro(request, cat_slug=None):
    category = None
    products_list = None

    if cat_slug!=None:
        category = get_object_or_404(Category, cat_slug=cat_slug)
        products_list = Product.objects.all().filter(pro_category=category, pro_is_available=True)
    else:
        products_list = Product.objects.all().filter(pro_is_available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except :
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'categorypage.html', {'category': category, 'products': products})


def ProductDetails(request, cat_slug, pro_slug):
    try:
        product = Product.objects.get(pro_category__cat_slug= cat_slug ,pro_slug= pro_slug)
    except Exception as exception:
        raise exception
    return render(request, 'productdetails.html', {'product': product})
