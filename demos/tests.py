from django.test import Client, TestCase

class DemoTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_divide_works_fine(self):
        response = self.client.get('/demos/divide?n=10&d=5')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(float(response.context['result']), 2.0)
        self.assertEqual(len(response.context['errors']), 0)

    def test_divide_by_zero(self):
        response = self.client.get('/demos/divide?n=10&d=0')

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.context['errors']), 0)