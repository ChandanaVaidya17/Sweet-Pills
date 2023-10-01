# myapp/urls.py

from django.urls import path
from .views import QuizResponseView

urlpatterns = [
    path('my-api-endpoint/', QuizResponseView.as_view(), name='my_api_endpoint'),
]
