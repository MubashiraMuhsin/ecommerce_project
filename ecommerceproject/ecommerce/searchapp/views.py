from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.


def SearchResult(request):
    products = None
    query = None

    if request.method == "GET":
        query = request.GET.get('search_term')
        print(query)
        products = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'products':products})