from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all()
        faq_data = []

        for faq in faqs:
            data = {
                'question': faq.get_translation(lang),
                'answer': faq.answer,
            }
            faq_data.append(data)

        return Response(faq_data, status=status.HTTP_200_OK)
