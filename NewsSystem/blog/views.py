from django.http import HttpResponse
from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

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
    return render(request, 'blog/about.html', {'title': 'О сайте'})


def login(request):
    return HttpResponse("Авторизация")


def contact(request):
    return HttpResponse("Связаться с нами")


def addpage(request):
    return HttpResponse("Добавление статьи")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id: {post_id}")


def page_not_found(request, exception):
    return HttpResponse("Страница не найдена")
