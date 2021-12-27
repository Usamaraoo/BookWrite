from django.contrib import admin
from .models import (Author, Book, Section)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'contributors_list')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sub_sec', 'book')


admin.site.register(Book, BookAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Author)
