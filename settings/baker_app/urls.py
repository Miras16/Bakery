
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signin/', views.login,name='login'),
    path('signup/', views.register,name='register'),
    path('about/', views.about,name='about'),
    path('blog/', views.blog,name='blog'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop,name='shop'),
    path('single-post/',views.single_post, name='single-post'),
    path('single-product/', views.single_product, name='single-product'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('logout/', views.logout, name='logout'),
]
