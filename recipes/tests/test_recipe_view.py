from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class Tests2(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        v = resolve(reverse('recipes:home'))
        self.assertIs(v.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        v = resolve(reverse('recipes:category', kwargs={ 'category_id': 1 }))
        self.assertIs(v.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        v = resolve(reverse('recipes:recipe', kwargs={ 'id': 1 }))
        self.assertIs(v.func, views.recipe)