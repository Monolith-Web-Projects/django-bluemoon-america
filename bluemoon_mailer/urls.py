from django.urls import path
from .views import send_email, get_csrf_token


urlpatterns = [
    path('send-email/', send_email),
    path('get-token/', get_csrf_token),
]