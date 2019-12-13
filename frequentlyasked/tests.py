from django.test import TestCase, Client
from django.urls import reverse, resolve

# Create your tests here.

class FAQUnitTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.faq = reverse('frequentlyasked:frequentlyasked')

    # Test Urls
    def test_FAQ_url_is_exist(self):
        url = self.client.get(self.faq)
        self.assertEquals(url.status_code, 200)