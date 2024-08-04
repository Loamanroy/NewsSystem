from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Bio', 'is_published': True},
    {'id': 2, 'title': 'Margo Robie', 'content': 'Bio', 'is_published': False},
    {'id': 3, 'title': 'Julie Roberts', 'content': 'Bio', 'is_published': True},
]


def index(request):
    data = {
        'title': "Главная страница",
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'blog/index.html', context=data)


def about(request):
    data = {
        'title': "О нас",
        'menu': menu
    }
    return render(request, 'blog/about.html', context=data)


def login(request):
    return HttpResponse("Авторизация")


def contact(request):
    return HttpResponse("Связаться с нами")


def add_page(request):
    return HttpResponse("Добавление статьи")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id: {post_id}")


def page_not_found(request, exception):
    return HttpResponse("Страница не найдена")
