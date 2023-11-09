from django.test import TestCase
from recipes.models import Category, Recipe, User


class TestBase(TestCase):
    def setUp(self):
        return super().setUp()

    def make_category(self, name='Categoria'):
        try:
            category = Category.objects.get(name=name)
            return category
        except:
            c = Category.objects.create(name=name)
            c.full_clean()
            c.save()
            return c

    def make_author(
        self,
        first_name='first name',
        last_name='last name',
        username='username',
        password='1234',
        email='username@email.com',
    ):
        
        try:
            author = User.objects.get(first_name=first_name)
            return author
        except:
            a = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
            )
            a.full_clean()
            a.save()
            return a

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
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
    ):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}
        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover
        )