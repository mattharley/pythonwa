from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from .models import Company


# Create your tests here.


class CompanyTest(TestCase):
    def setUp(self):
        pass

    def test_company_home(self):
        client = Client()
        response = client.get(reverse('companies-home'))
        self.assertEqual(response.status_code, 200)

    def test_company_creation(self):
        client = Client()
        response = client.post(reverse('companies-create'),
                               {'name': 'jose', 'abn': '12312423422377777777', 'description': 'my description',
                                'logo': open('./android-icon.png')})

        self.assertIn("Record succesfully created", response.content)

        num_companies = Company.objects.count()
        self.assertEqual(num_companies, 1)

        company = Company.objects.all()[0]
        self.assertEqual(company.name, "josej")
