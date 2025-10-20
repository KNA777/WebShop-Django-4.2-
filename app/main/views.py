from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'Главная страница Web Shop',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О Нас',
        'content': 'О НАС',
        'text_on_page': 'Some text'
    }
    return render(request, 'main/about.html', context)
