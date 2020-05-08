from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Dish URLs
    path('add_dish', views.add_dish, name='add_dish'),
    path('edit_dish/<int:dish_id>', views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:dish_id>', views.delete_dish, name='delete_dish'),

    # Recipe URLs
    path('recipes/<int:dish_id>', views.recipes, name='recipes'),
    path('add_recipe/<int:dish_id>', views.add_recipe, name='add_recipe'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe')

]