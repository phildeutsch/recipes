from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),

    # Account URLs
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),

    # Dish URLs
    path('dishes', views.dishes, name='dishes'),
    path('dish/<int:dish_id>', views.recipes, name='recipes'),
    path('add_dish', views.add_dish, name='add_dish'),
    path('edit_dish/<int:dish_id>', views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:dish_id>', views.delete_dish, name='delete_dish'),

    # Recipe URLs
    path('add_recipe/<int:dish_id>', views.add_recipe, name='add_recipe'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),

    # Guest URLs
    path('guests', views.guests, name='guests'),
    path('add_guest', views.add_guest, name='add_guest'),

    # Activity URLs
    path('activities', views.activities, name='activities'),
    path('add_activity', views.add_activity, name='add_activity')
]