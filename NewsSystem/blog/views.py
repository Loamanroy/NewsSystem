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

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям<p>id: {cat_id}</p></h1>")
