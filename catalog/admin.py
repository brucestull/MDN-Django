from django.contrib import admin

from catalog import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth')


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book)
admin.site.register(models.BookInstance)
admin.site.register(models.Genre)
admin.site.register(models.Language)
