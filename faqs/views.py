from django.shortcuts import render
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
<<<<<<< HEAD
=======
from django.core.cache import cache
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
<<<<<<< HEAD
        queryset = FAQ.objects.all()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
=======
        cache_key = f'faqs_{lang}'
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = FAQ.objects.all()
            for faq in queryset:
                faq.question = faq.get_translated_question(lang)
                faq.answer = faq.get_translated_answer(lang)
            cache.set(cache_key, queryset, timeout=60*15)  # Cache for 15 minutes
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
        return queryset