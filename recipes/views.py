from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Dish, Recipe
from .forms import DishForm, RecipeForm

@login_required
def index(request):
    dishes = Dish.objects.filter(user=request.user)

    context = {'dishes': dishes}
    return render(request, 'recipes/index.html', context)

# Dish views
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
    if dish.picture:
        dish.picture.delete()
    if dish.user==request.user:
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
    dishes = Dish.objects.filter(user=request.user)
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
            return redirect('/recipes/'+str(dish_id))
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form, 'dish': dish})

@login_required
def pin_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.dish.user==request.user:
        recipe.pinned = 1 - recipe.pinned
        recipe.save()
    return redirect('/recipes/'+str(recipe.dish.id))

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.dish.user==request.user:
        recipe.delete()
    return redirect('/recipes/'+str(recipe.dish.id))

@login_required
def modify_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    # recipe.id = None
    form = RecipeForm(instance=recipe)
    context ={'recipe': recipe, 'form': form}

    if request.method == "POST":
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.parent_recipe = None
            post.pinned = False
            post.save()
            return redirect('/recipes/'+str(recipe.dish.id))

    return render(request, 'recipes/modify_recipe.html', context)


@login_required
def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context ={'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)
