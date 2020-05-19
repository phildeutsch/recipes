from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Dish, Recipe
from .forms import DishForm, RecipeForm

from accounts.models import User, Profile

@login_required
def index(request):
    dishes = Dish.objects.all()

    context = {'dishes': dishes}
    return render(request, 'recipes/index.html', context)

@login_required
def users(request):
    users = User.objects.all()
    context = {'users': users} 
    return render(request, 'users/users.html', context)

# Dish views
@login_required
def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = DishForm()

    return render(request, 'recipes/add_dish.html', {'form': form})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if dish.picture:
        dish.picture.delete()
        dish.delete()
    return redirect('/')

@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            post = form.save()
            return redirect('/')
    else:
        form = DishForm(instance=dish)
    
    context = {'form': form, 'dish': dish}
    return render(request, 'recipes/edit_dish.html', context)

# Recipe views
@login_required
def recipes(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    dishes = Dish.objects.all()
    recipes = Recipe.objects.filter(dish=dish)

    context = {
        'dishes': dishes,
        'dish_id': dish_id,
        'recipes': recipes}

    return render(request, 'recipes/index.html', context)

@login_required
def add_recipe(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.dish = dish
            post.parent_recipe = None
            post.pinned = False
            post.save()
            return redirect('/recipes/dish/'+str(dish_id))
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form, 'dish': dish})

@login_required
def pin_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.pinned = 1 - recipe.pinned
    recipe.save()
    return redirect('/recipes/dish/'+str(recipe.dish.id))

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('/recipes/dish/'+str(recipe.dish.id))

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.id = None
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            post = form.save(commit=False)
            post.parent_recipe = get_object_or_404(Recipe, pk=recipe_id)
            post.pinned = False
            post.save()
            return redirect('/recipes/recipe/' + str(recipe.id))
    else:
        form = DishForm(instance=recipe)
    
    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipes/edit_recipe.html', context)


@login_required
def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context ={'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)
