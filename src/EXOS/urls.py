
from django.contrib import admin
from django.urls import path
from orm_practice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view(), name = 'books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name= 'detail_book'),
    path('authors/', views.AuthorListView.as_view(), name = 'authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name = 'detail_author')
]
