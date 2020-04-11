from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Dish

@login_required
def index(request):
    dishes = Dish.objects.filter(user=request.user)

    context = {'dishes': dishes}
    return render(request, 'recipes/index.html', context)
