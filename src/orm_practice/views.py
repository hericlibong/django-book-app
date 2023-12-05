from django.shortcuts import render
from orm_practice.models import Author, Book
from django.views.generic import ListView, DetailView



class BookListView(ListView):
    model = Book
    template_name = 'orm_practice/list_book.html'
    context_object_name = 'list_books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'orm_practice/detail_book.html'
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Author
    template_name = 'orm_practice/list_author.html'
    context_object_name = 'list_authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'orm_practice/detail_author.html'
    context_object_name = 'author'
    

