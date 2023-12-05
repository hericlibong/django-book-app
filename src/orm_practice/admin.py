from django.contrib import admin
from .models import Author, Book



class AuthorAdmin(admin.ModelAdmin):
    
    fields = ['name', 'birth_date', 'biography']



class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'is_bestseller',
            'rating', 'pub_year', 'price', 'discount']
    



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

