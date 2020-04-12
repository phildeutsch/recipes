from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Dish
from .forms import DishForm

@login_required
def index(request):
    dishes = Dish.objects.filter(user=request.user)

    context = {'dishes': dishes}
    return render(request, 'recipes/index.html', context)

@login_required
def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
    else:
        form = DishForm()

    return render(request, 'recipes/add_dish.html', {'form': form})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if dish.user==request.user:
        dish.delete()
    return redirect('/')

@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            post = form.save()
            return redirect('/')
    else:
        form = DishForm(instance=dish)
    
    context = {'form': form, 'dish': dish}
    return render(request, 'recipes/edit_dish.html', context)