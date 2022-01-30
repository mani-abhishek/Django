from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("temple",views.temple,name='temple'),
    path("arts",views.arts,name='arts'),
    path("books",views.books,name='books'),
]