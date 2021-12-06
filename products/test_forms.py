from django.test import TestCase
from .forms import ProductForm


# Test product form
class TestProductForms(TestCase):

    def test_create_product_form_incomplete(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())


    def test_create_product_form_complete(self):
        form = ProductForm({
            'category': 'Basketballs',
            'sku': 'hp03',
            'name': 'Champro Indoor Basketball',
            'description': 'The Champro Phoenix is an excellent quality \
                indoor basketball for beginners on a budget.',
            'has_sizes': False,
            'price': '19.99',
            'rating': '3.80',
            'image_url': 'https://drive.google.com/file/d/1l0TbPjapVyvRsjV06ltQyIneBZjiXQN-/view?usp=sharing',
            'image': ''})
        self.assertFalse(form.is_valid())
