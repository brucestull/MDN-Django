from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of catalog application.
    """

    # General counts of Book, BookInstance, and Genre.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre = Genre.objects.count()

    # Number of available BookInstances.
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Number of Authors.
    # Either statement should work. 'all()' is implied in 'Author.objects'.
    num_authors = Author.objects.count()
    # num_authors = Author.objects.all().count()

    # Some stats on various titles:
    the_titles = Book.objects.filter(title__contains='the').count()
    book_titles = Book.objects.filter(title__contains='book').count()
    my_titles = Book.objects.filter(title__contains='my').count()

    # Number of books by language:
    num_python = BookInstance.objects.filter(language__name__iexact='python').count()
    num_arabic = BookInstance.objects.filter(language__name__iexact='arabic').count()

    # Some specific available books:
    num_instances_available_book = BookInstance.objects.filter(status__exact='a').filter(book__title__contains='book').count()
    instances_available_book = BookInstance.objects.filter(status__exact='a').filter(book__title__contains='book')


    # Build the context dictionary-object:
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'the_titles': the_titles,
        'book_titles': book_titles,
        'my_titles': my_titles,
        'num_instances_available_book': num_instances_available_book,
        'instances_available_book': instances_available_book,
        'num_python': num_python,
        'num_arabic': num_arabic,
    }

    # Send arguments to 'render':
    return render(request, 'index.html', context=context)

