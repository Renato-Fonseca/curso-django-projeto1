from django.test import TestCase
from django.urls import reverse

from recipes.models import Category, Recipe, User


class Test_responses(TestCase):
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
        response = self.client.get(reverse('recipes:home'))
        cont = response.content.decode('utf-8')
        self.assertIn('<div id="no-recipes">Ops, parece que ninguém postou receitas ainda, tenha a honra de ser o primeiro!</div>', cont)

   # def test_recipe_home_template_loads_recipes(self):
   #     category = Category.objects.create(name='Categoria')
   #     category.full_clean()
    #    category.save()
    #    author = User.objects.create(
      #      first_name='first name',
      #      last_name='last name',
     #       username='username',
     # #      password='1234'
      #      email='username@email.com'
      #      )  
       # recipe = Recipe.objects.create(
       #     category=category
      #      author=author
       #     title='titúlo'
       #     description='Descrição'
      #      slug='slug'
      #      preparation_time=12
      #      preparation_time_unit='minutos'
      #      servings=8
      #      servings_unit='pedaços'
     #       preparation_steps='Passos para o preparo'
     #       preparation_steps_is_html=False
    #        is_published=True
    #    )
    #    assert 1 == 1
        