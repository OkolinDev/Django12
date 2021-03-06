from django.shortcuts import render

from .models import Product


def main(request):
    title = "Главная"
    products = Product.objects.all()
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    title = "Продукты"
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'title': title,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    return render(request, 'mainapp/contact.html')
