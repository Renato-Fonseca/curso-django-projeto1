from .test_recipe_base import TestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Category


class CategoryModelTest(TestBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()
    
    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name, msg=f'needed {self.category.name}, but {str(self.category)} was received')
    
    def test_category_fields_max_length(self):
        value = 'A' * 66
        self.category.name = value

        with self.assertRaises(ValidationError):
            self.category.full_clean()        
