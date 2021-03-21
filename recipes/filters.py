import django_filters
from .models import Dish, Recipe
from django.utils.translation import ugettext_lazy as _

class DishFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    course = django_filters.ChoiceFilter(choices=Dish.DISH_COURSE_CHOICES, label=_("Course"))
    cuisine = django_filters.ChoiceFilter(choices=Dish.DISH_CUISINE_CHOICES, label=_("Cuisine"))

class RecipeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    course = django_filters.ChoiceFilter(choices=Recipe.COURSE_CHOICES, label=_("Course"))
    cuisine = django_filters.ChoiceFilter(choices=Recipe.CUISINE_CHOICES, label=_("Cuisine"))
    vegetarian = django_filters.BooleanFilter()
    meat = django_filters.BooleanFilter()
    fish = django_filters.BooleanFilter()
