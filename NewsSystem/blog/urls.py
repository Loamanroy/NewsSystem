from django.contrib import admin
from django.urls import path, include

from blog.views import index, about, categories

urlpatterns =[
    path('', index, name="home"),
    path('about/', about, name="О нас"),
    path('cats<int:pk>', categories, name="cats_id"),
]