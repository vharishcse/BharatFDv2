from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faqs.views import FAQViewSet
from django.http import HttpResponse

# Home view
def home(request):
    return HttpResponse("Welcome to BharatFD Internship Test!")

# Register FAQViewSet with the router
router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('api/', include(router.urls)),  # API endpoints
    path('', home, name='home'),  # Root URL
]