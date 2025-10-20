from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница Web Shop',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О Нас',
        'content': 'О НАС',
        'text_on_page': 'Some text'
    }
    return render(request, 'main/about.html', context)
