from django.test import TestCase, Client
from main.models import Product

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_url_is_exist(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_contains_expected_data(self):
        response = self.client.get('/main/')
        # Ensure that the rendered HTML contains data from your context
        self.assertContains(response, 'Masabil Arraya Muhammad')
        self.assertContains(response, 'PBP A')
        self.assertContains(response, 'SDA')
        self.assertContains(response, 'Statprob')
        self.assertContains(response, 'REVIEW MATKUL')

    def test_product_model(self):
        # Create a test Product instance
        product = Product.objects.create(
            name='Test Product',
            classes='A',
            description='Test description',
            amount=50,
            nilai='A'
        )
        # Query the database to check if the product was created
        saved_product = Product.objects.get(id=product.id)
        self.assertEqual(saved_product.name, 'Test Product')

    def test_invalid_main_url_returns_404(self):
        response = self.client.get('/invalid_url/')
        self.assertEqual(response.status_code, 404)

