from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_dish', views.add_dish, name='add_dish')
]