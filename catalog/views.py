from django.shortcuts import render

from catalog.models import Book, BookInstance
from catalog.models import Genre, Language, Author


def the_word(request):
    context = {
        'the_word': 'bangers and mash'
    }
    return render(request, 'catalog/the_word.html', context=context)


def index(request):
    # print('dir(request): ', dir(request))
    # print('dir(request.GET): ', dir(request.GET))

    num_books = Book.objects.count()
    print('num_books: ', num_books)
    num_instances = BookInstance.objects.all().count()
    print('num_instances: ', num_instances)
    
    # Some counts of catagories:-
    num_arabic = BookInstance.objects.filter(language__name__iexact='arabic').count()
    print('num_arabic: ', num_arabic)
    num_english = BookInstance.objects.filter(language__name__iexact='english').count()
    print('num_english: ', num_english)

    # Available books for loan:
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    print('num_instances_available: ', num_instances_available)

    # Number of authors:
    num_authors = Author.objects.count()
    print('num_authors: ', num_authors)

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_arabic': num_arabic,
        'num_english': num_english,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'catalog/index.html', context=context)


