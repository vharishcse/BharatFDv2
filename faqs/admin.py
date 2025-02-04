from django.contrib import admin
<<<<<<< HEAD
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
=======
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import FAQ

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditor5Widget(config_name='default'),
        }

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'question_hi', 'question_bn')
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
