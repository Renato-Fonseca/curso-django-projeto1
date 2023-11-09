from .test_recipe_base import TestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Recipe


class RecipeModelTest(TestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    @parameterized.expand([
                ('title', 65),
                ('description', 165),
                ('preparation_time_unit', 65),
                ('servings_unit', 65),
            ])
    

    def test_recipe_fields_max_length(self, field, maxLength):
        value = 'A' * (maxLength + 1)
        setattr(self.recipe, field, value)
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    

    @parameterized.expand(
            [('preparation_steps_is_html', {'default': False}),
            ('is_published', {'default': False}),]
    )
    def test_recipe_fields_defaults(self, field, kwargs):
        recipe = Recipe(
            category=self.make_category(),
            author=self.make_author(),
            title='titúlo',
            description='Descrição',
            slug='slug',
            preparation_time=12,
            preparation_time_unit='minutos',
            servings=8,
            servings_unit='pedaços',
            preparation_steps='Passos para o preparo',
            cover='recipes/covers/2023/07/25/sorvete-de-chocolate-848x477.jpg'
        )
        recipe.full_clean()
        recipe.save()
        atribute = getattr(recipe, field)
        if kwargs['default'] is True:
            self.assertTrue(atribute)
        else:
            self.assertFalse(atribute)
        # self.assertEqual(atribute, kwargs['default'])


    def test_recipe_string_representation(self):
        needed = 'Um título'
        self.recipe.title = 'Um título'
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(str(self.recipe), needed,
                         msg=f"needed {needed}, but {str(self.recipe)} was received")
        
