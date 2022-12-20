from django.shortcuts import render
from shops.models import Category, Product
from django.db.models import Q


def SearchFunction(request):
    products = None
    query = None
    if 'search_word' in request.GET:
        word = request.GET['search_word']
        products = Product.objects.all().filter(Q(pro_name__contains=word)|Q(pro_desc__contains=word))
        print("products", products)
    context = {
        'search_word': word,
        'products': products,
    }

    return render(request, 'searchresult.html', context)



