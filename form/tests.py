from django.test import TestCase, Client
from django.urls import reverse, resolve
from form.views import contact, feedback
from form.models import FeedbackForm 
from form.forms import FieldForm
from django.conf import settings

# Create your tests here.

class unitTestFormApp(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact = reverse('form:contact')
        self.feedback = reverse('form:feedbackform')

    # Test urls
    def test_contact_url_is_exist(self):
        response =  self.client.get('/')
        self.assertEquals(response.status_code, 302)

    def test_feedback_redirect_when_unauthenticated(self):
        response = self.client.get(self.feedback)
        self.assertEquals(response.status_code, 302)

    # Test views
    def test_contact_render_templates(self):
        response = self.client.get(self.contact)
        self.assertTemplateUsed(response, 'contact/index.html')

    def test_contact_url_using_contact_func(self):
        url = self.contact
        self.assertEquals(resolve(url).func, contact)

    def test_feedback_url_using_feedback_func(self):
        url = self.feedback
        self.assertEquals(resolve(url).func, feedback)
        
    # Test models
    def test_field_forms_notValid(self):
        form = FieldForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_forms_success_make_models_and_matches(self):
        data = FeedbackForm.objects.create(
            Satisfaction ='10',
        )
        counting_all_data = FeedbackForm.objects.all().count()
        self.assertEquals(counting_all_data, 1)
        self.assertTrue(isinstance(data, FeedbackForm))
        self.assertEquals(data.__str__(), data.Satisfaction)
    






