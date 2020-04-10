from django.shortcuts import render

from .models import Dish

def index(request):
    dishes = Dish.objects.all()

    context = {'dishes': dishes}
    return render(request, 'recipes/index.html', context)
