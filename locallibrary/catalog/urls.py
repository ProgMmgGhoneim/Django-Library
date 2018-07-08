from django.urls import path , include

from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('aboutus/',AboutTemplateView.as_view() ,name='about_us'),
    path('books/',BookListView.as_view() ,name='book'),
    path('books/<int:pk>',BookDetailsView.as_view() ,name='book-detail'),
    path('authors/',AuthorListView.as_view() ,name='author'),
    path('authors/<int:pk>',AuthorDetailsView.as_view() ,name='author-details'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('books/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('authors/create/', AuthorCreate.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    path('books/create/', BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),


]
