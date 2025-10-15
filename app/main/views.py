from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница Web Shop'
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('Информация о странице')
