from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #model = Author
    fields = ['name']
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #model = Book
    fields = ['title', 'author','is_bestseller',
            'rating', 'pub_year', 'price', 'discount']



# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)

