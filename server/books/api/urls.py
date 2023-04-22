from .views import bookAPIView
from django.urls import path

app_name = 'api-books'

urlpatterns = [
    path('', bookAPIView.as_view(), name='book-create'),
]