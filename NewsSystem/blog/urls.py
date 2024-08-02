from django.contrib import admin
from django.urls import path

from blog.views import index, about, show_post, addpage, contact, login

urlpatterns =[
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('addpage/', addpage, name="addpage"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('post/<int:post_id>/', show_post, name="post")
]