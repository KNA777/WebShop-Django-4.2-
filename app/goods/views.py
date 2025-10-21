from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Products


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category_id__slug=category_slug))

    paginator = Paginator(goods, per_page=3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)
