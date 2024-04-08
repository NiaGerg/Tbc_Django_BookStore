from django.http import JsonResponse
from .models import Book


def get_books(request):
    books = Book.objects.all().order_by('name')
    return_books = []
    for book in books:
        return_books.append({
            'name': book.name,
            'page_count': book.page_count,
            'category': book.category,
            'author_name': book.author_name,
            'price': str(book.price),
            'image_url': book.image.url if book.image else None,
        })
    return JsonResponse(return_books, safe=False)
