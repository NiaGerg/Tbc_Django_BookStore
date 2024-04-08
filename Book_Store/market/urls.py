from django.urls import path
from market.views import get_books

urlpatterns = [
    path('books/', get_books, name='books'),
]