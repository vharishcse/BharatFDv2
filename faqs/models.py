from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
<<<<<<< HEAD
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    try:
        return translator.translate(text, dest=dest_lang).text
    except:
        return text

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field('Answer', config_name='extends')
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = CKEditor5Field(blank=True, null=True)  # Hindi
    answer_bn = CKEditor5Field(blank=True, null=True)  # Bengali

    def get_translated_question(self, lang='en'):
        if lang == 'en':
            return self.question
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        if lang == 'en':
            return self.answer
        return getattr(self, f'answer_{lang}', self.answer)
    
    def save(self, *args, **kwargs):
        self.question_hi = translate_text(self.question, 'hi')
        self.question_bn = translate_text(self.question, 'bn')
        self.answer_hi = translate_text(self.answer, 'hi')
        self.answer_bn = translate_text(self.answer, 'bn')
=======
from googletrans import Translator  

# Create an instance of the Translator
translator = Translator()

# Define a function to translate text
def translate_text(text, dest_lang):
    try:
        # Use the translator to translate the text to the target language
        return translator.translate(text, dest=dest_lang).text
    except:
        # If translation fails, return the original text as a fallback
        return text
    
class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field('Answer', config_name='default')
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = models.TextField(blank=True, null=True)    # Hindi
    answer_bn = models.TextField(blank=True, null=True)    # Bengali

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer)

    def save(self, *args, **kwargs):  # Step 6.2: Automate Translations
        # Translate the question into Hindi if the field is empty
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        
        # Translate the question into Bengali if the field is empty
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        
        # Translate the answer into Hindi if the field is empty
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        
        # Translate the answer into Bengali if the field is empty
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')
        
        # Call the parent class's save method to save the FAQ object
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question