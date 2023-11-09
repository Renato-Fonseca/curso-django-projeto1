from django.test import TestCase
from django.urls import reverse
from recipes.models import Category, Recipe, User
from .test_recipe_base import TestBase


class Test_responses(TestBase):
    def test_recipe_home_view_returns_status_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={ 'category_id': 10000 }))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_doesnt_show_recipes_that_arent_published(self):
        cd = {'name': 'Lanches'}
        defaultRecipe = self.make_recipe(category_data=cd)
        myRecipe = self.make_recipe(title='Cachorro Quente Rascunho', is_published=False, category_data=cd) 

        response = self.client.get(reverse('recipes:category', kwargs={'category_id': myRecipe.category.id}))
        cont = response.content.decode('utf-8')
        self.assertNotIn('<h2 class="recipe-title">Cachorro Quente Rascunho</h2>', cont) # ele não postou a receita.

    def test_recipe_category_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIn('<div class="recipe-content">', response.content.decode('utf-8'))


    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={ 'id': 10000 }))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_doesnt_show_the_recipe_if_it_is_not_published(self):
       defaultRecipe = self.make_recipe(is_published=False)

       response = self.client.get(reverse('recipes:recipe', kwargs={'id': defaultRecipe.id}))
       cont = response.content.decode('utf-8')
       
       self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self): 
        self.make_recipe(title='Coxinha')
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIn('<h2 class="recipe-title">Coxinha</h2>', response.content.decode('utf-8')) 


    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_none_exist(self):
       response = self.client.get(reverse('recipes:home'))
       cont = response.content.decode('utf-8')
       self.assertIn('<div id="no-recipes">Ops, parece que ninguém postou receitas ainda, tenha a honra de ser o primeiro!</div>', cont)

    def test_recipe_home_template_doesnt_show_recipes_if_none_is_published(self):
       self.make_recipe(is_published=False)

       response = self.client.get(reverse('recipes:home'))
       cont = response.content.decode('utf-8')
       self.assertIn('<div id="no-recipes">Ops, parece que ninguém postou receitas ainda, tenha a honra de ser o primeiro!</div>', cont) 

    def test_recipe_home_template_loads_recipes(self):  
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<div class="recipe-content">', response.content.decode('utf-8'))
