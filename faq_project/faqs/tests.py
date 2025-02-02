from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डजांगो क्या है?",
            question_bn="ডjango কি?",
        )

    def test_translation_method(self):
        self.assertEqual(self.faq.get_translation('hi'), "डजांगो क्या है?")
        self.assertEqual(self.faq.get_translation('bn'), "ডjango কি?")
        self.assertEqual(self.faq.get_translation('en'), "What is Django?")

    def test_auto_translation(self):
        new_faq = FAQ.objects.create(question="What is Python?", answer="Python is a programming language.")
        self.assertIsNotNone(new_faq.question_hi)
        self.assertIsNotNone(new_faq.question_bn)
