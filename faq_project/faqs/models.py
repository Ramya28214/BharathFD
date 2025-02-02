from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField("Question")
    answer = RichTextField("Answer")

    question_hi = models.TextField("Question (Hindi)", null=True, blank=True)
    question_bn = models.TextField("Question (Bengali)", null=True, blank=True)

    def get_translation(self, lang_code='en'):
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang_code, self.question)

    def __str__(self):
        return self.question
