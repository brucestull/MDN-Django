from django.contrib import admin

from catalog import models

# Used to display a tabular view of BookInstance within a related model's admin page.
class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1


# Used to display a tabular view of Book within a related model's admin page.
class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1


###### Alternate ways to register Book and BookAdmin ######
# Decorator use:
# - Model 'Book' as argument in '@admin.register()'.
# - Class 'BookAdmin' is used to specify admin page attributes and properties.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    #  List View:
    # Specify which fields to display in list view.
    list_display = ('title', 'author', 'display_genre', 'genre_list')
    # Specify which fields are to be used for filtered view.
    list_filter = ('title', 'author')

    # Detail-Edit View:
    # Specify which 'Inline's are to be included in detail-edit view.
    inlines = (BookInstanceInline,)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# class BookAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(models.Book, BookAdmin)
#
###########################################################

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):

    # List View:
    # Fields to display in 'Author' list view.
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # Specify which fields are to be used for filtered view.
    list_filter = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Detail-Edit View:
    # Fields to display in 'Author' detail-edit view.
        # Group fields by parens within main tuple to specify grouping and position.
    fields = ('last_name', 'first_name', ('date_of_birth', 'date_of_death'))
    # Specify which 'Inline's are to be included in detail-edit view.
    inlines = (BookInline,)


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    # List View:
    # Specify which fields to display in BookInstance List View.
    list_display = ('book', 'get_author', 'language', 'get_genre', 'status', 'due_back')
    # Specify which fields to use for filtering in BookInstance List View.
    list_filter = ('status', 'due_back', 'language', 'imprint')

    # Detail-Edit View:
    # Specify display, grouping, and labeling of fields in Detail-Edit View.
    fieldsets = (
        # Fieldset can display no group label (use 'None') or be specified by a string.
        # (None, {
        ('Book Details', {
            'fields': ('language', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )


admin.site.register(models.Genre)
admin.site.register(models.Language)
