from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import login
from .models import User

# Create your tests here.

class getReceiptsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.force_login(self.user)

    def test_view_status_code(self):
        url = reverse('my_receipts') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        url = reverse('my_receipts')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'all_receipts.html')