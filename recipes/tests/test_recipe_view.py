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

    def test_recipe_search_view_function_is_correct(self):
        v = resolve(reverse('recipes:search'))
        self.assertIs(v.func, views.search)

    def test_recipe_search_template_is_correct(self):
        response = self.client.get(reverse('recipes:search') + '?q=testando')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
