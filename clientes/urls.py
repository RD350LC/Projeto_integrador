from django.urls import path
from django.http import HttpResponse

app_name = 'clientes'  # Ensure this is correctly set

# Placeholder view for testing
def test_view(request):
    return HttpResponse("Test view is working!")

urlpatterns = [
    path('test/', test_view, name='test'),  # Add a test URL pattern
]