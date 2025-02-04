from django.test import TestCase
<<<<<<< HEAD
from django.urls import reverse
from rest_framework.test import APIClient
from faqs.models import FAQ

class FAQAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="Django क्या है?",
            answer_hi="Django एक वेब फ्रेमवर्क है।",
            question_bn="জ্যাঙ্গো কী?",
            answer_bn="জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_fetch_faqs_in_bengali(self):
        response = self.client.get(reverse('faq-list'), {'lang': 'bn'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question_bn'], "জ্যাঙ্গো কী?")
        self.assertEqual(response.data[0]['answer_bn'], "জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।")

    def test_fetch_faqs_in_english(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is Django?")
        self.assertEqual(response.data[0]['answer'], "Django is a web framework.")
=======
from .models import FAQ

class FAQTests(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        self.assertEqual(faq.question, "What is Django?")
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
