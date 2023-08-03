from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.blog, name='about'),
    path('<str:slug>/', views.blogpost, name='blogpost'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('login', views.login_page, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('logout', views.logout_page, name="logout"),
    # path('comm', views.comment, name="comm")

]
