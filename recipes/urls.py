from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('users', views.users, name='users'),

    # Dish URLs
    path('recipes/dish/<int:dish_id>', views.recipes, name='recipes'),
    path('recipes/add_dish', views.add_dish, name='add_dish'),
    path('recipes/edit_dish/<int:dish_id>', views.edit_dish, name='edit_dish'),
    path('recipes/delete_dish/<int:dish_id>', views.delete_dish, name='delete_dish'),

    # Recipe URLs
    path('recipes/add_recipe/<int:dish_id>', views.add_recipe, name='add_recipe'),
    path('recipes/delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('recipes/pin_recipe/<int:recipe_id>', views.pin_recipe, name='pin_recipe'),
    path('recipes/modify_recipe/<int:recipe_id>', views.modify_recipe, name='modify_recipe'),
    path('recipes/recipe/<int:recipe_id>', views.recipe, name='recipe')

]