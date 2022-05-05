from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    """
    Model for book genre.
    """
    name = models.CharField(
        max_length=200,
        help_text='Enter the book genre (fiction, non-fiction, science, science fiction, etc)'
    )

    def __str__(self):
        """
        String representation of Genre Model object.
        """
        return self.name


class Language(models.Model):
    """
    Model for content Language (Arabic, English, French, Spanish, etc.).
    """
    name = models.CharField(
        max_length=200,
        help_text="""
            Enter the content's natural language (Arabic, English, 
            French, Spanish, etc.).
        """
        )
    
    
    def __str__(self):
        """
        String representation of Language Model object.
        """
        return self.name


class Book(models.Model):
    """
    Model for book.
    """
    title = models.CharField(
        max_length=200
    )
    author = models.ForeignKey(
        'author',
        on_delete=models.SET_NULL,
        null=True,
        help_text='Enter the author of the book.'
    )
    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the book.'
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>.'
    )
    genre = models.ManyToManyField(
        Genre,
        help_text='Select a genre for this book'
    )
    
    def __str__(self):
        """
        String representation of the Book Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a particular BookInstance.
        """
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:4])
    
    def genre_list(self):
        return tuple(genre.name for genre in self.genre.all()[:4])
    
    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """
    Model for specific instances of Book Model. This represents the objects which are checked out of the library.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book instance."
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.RESTRICT,
        null=True
    )
    imprint = models.CharField(
        max_length=200
    )
    due_back = models.DateField(
        null=True,
        blank=True
    )
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability.'
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        """
        String representation for BookInstance Model object.
        """
        return f'{ self.book.title} ({ self.id })'
    
    def get_author(self):
        return self.book.author


class Author(models.Model):
    """
    Model for content Author.
    """
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    date_of_birth = models.DateField(
        'Birth',
        null=True,
        blank=True
    )
    date_of_death = models.DateField(
        'Deceased',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """
        Returns the URL to access a particular Author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String representation of Author Model object.
        """
        return f'{ self.last_name }, { self.first_name }'


    