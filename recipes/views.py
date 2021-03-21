from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dateutil import parser

from .models import Dish, Recipe, Guest, Activity
from .forms import DishForm, RecipeForm, GuestForm, ActivityForm
from .filters import DishFilter, RecipeFilter

from accounts.models import User, Profile
from accounts.forms import ProfileForm

@login_required
def index(request):
    return redirect('/activities')

@login_required
def dashboard(request):
    context = {} 
    return render(request, 'dashboard.html', context)

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).get()
    context = {'p': profile} 
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).get()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            post = form.save()
            return redirect('/profile')
    else:
        form = ProfileForm(instance=profile)
    
    context = {'form': form, 'p': profile}
    return render(request, 'accounts/edit_profile.html', context)

# Dish views
@login_required
def dishes(request):
    dishes = Dish.objects.all()
    f = DishFilter(request.GET, queryset=dishes)

    context = {'dishes': dishes, 'filter': f}
    return render(request, 'recipes/dishes.html', context)

@login_required
def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/dishes')
    else:
        form = DishForm()

    return render(request, 'recipes/add_dish.html', {'form': form})

@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if dish.picture:
        dish.picture.delete()
    dish.delete()
    return redirect('/dishes')

@login_required
def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            post = form.save()
            return redirect('/dishes')
    else:
        form = DishForm(instance=dish)
    
    context = {'form': form, 'dish': dish}
    return render(request, 'recipes/edit_dish.html', context)

@login_required
def dish_recipes(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    recipes = Recipe.objects.filter(dish=dish).all()

    context = {'dish': dish, 'recipes': recipes}

    return render(request, 'recipes/dish_recipes.html', context)

# Recipe views
@login_required
def recipes(request):
    recipes = Recipe.objects.filter().all()
    f = RecipeFilter(request.GET, queryset=recipes)

    context = {'recipes': recipes, 'filter': f}

    return render(request, 'recipes/recipes.html', context)

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/dish/'+str(dish_id))
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('/dish/'+str(recipe.dish.id))

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            post = form.save()
            return redirect('/recipe/' + str(recipe.id))
    else:
        form = RecipeForm(instance=recipe)
    
    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipes/edit_recipe.html', context)

@login_required
def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context ={'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)

# Guest views
@login_required
def guests(request):
    guests = Guest.objects.filter(user=request.user)

    context = {'guests': guests}
    return render(request, 'guests/guests.html', context)

@login_required
def add_guest(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/guests')
    else:
        form = GuestForm()

    return render(request, 'guests/add_guest.html', {'form': form})

# Activity views
@login_required
def activities(request):
    activities = Activity.objects.filter(user=request.user)
    context = {'activities': activities}
    return render(request, 'activities/activities.html', context)

@login_required
def add_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/activities')
    else:
        form = ActivityForm(user=request.user)

    return render(request, 'activities/add_activity.html', {'form': form})