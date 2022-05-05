from django.contrib import admin

from catalog import models


class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1


class BookInline(admin.TabularInline):
    model = models.Book
    extra = 1


###### Alternate ways to register Book and BookAdmin ######

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
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
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('last_name', 'first_name', ('date_of_birth', 'date_of_death'))
    inlines = (BookInline,)
    list_filter = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'status', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    list_filter = ('status', 'due_back', 'imprint')


admin.site.register(models.Genre)
admin.site.register(models.Language)
