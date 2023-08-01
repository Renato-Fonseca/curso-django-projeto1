from django.test import TestCase
from django.urls import reverse
from recipes.models import Category, Recipe, User
from .test_recipe_base import Test_Base


class Test_responses(Test_Base):

    def test_recipe_home_view_returns_status_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={ 'category_id': 10000 }))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={ 'id': 10000 }))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_none_exist(self):
        Recipe.objects.get(pk=1).delete() # era pra isso ter funcionado...
        response = self.client.get(reverse('recipes:home'))
        cont = response.content.decode('utf-8')
        self.assertIn('<div id="no-recipes">Ops, parece que ninguém postou receitas ainda, tenha a honra de ser o primeiro!</div>', cont)

    def test_recipe_home_template_loads_recipes(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertIn('<span class="main-logo-text">Recipes</span>', response.content.decode('utf-8'))
        assert response.context['is_detail_page'] == False
