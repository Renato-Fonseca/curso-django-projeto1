from django.test import TestCase
from recipes.models import Category, Recipe, User


class Test_Base(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Categoria')
        category.full_clean()
        category.save()
        author = User.objects.create(
            first_name='first name',
            last_name='last name',
            username='username',
            password='1234',
            email='username@email.com'
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='titúlo',
            description='Descrição',
            slug='slug',
            preparation_time=12,
            preparation_time_unit='minutos',
            servings=8,
            servings_unit='pedaços',
            preparation_steps='Passos para o preparo',
            preparation_steps_is_html=False,
            is_published=True,
            cover='recipes/covers/2023/07/25/sorvete-de-chocolate-848x477.jpg'
        )