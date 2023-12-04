from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    is_bestseller = models.BooleanField(default=False)
    pub_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2023)], 
                                   null=True, blank=True, default=2023)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title
    
    class Meta : 
        ordering = ['-pub_year']


# Récupérer la liste des livres qui ont un classement supérieur à 8.
# Trouver les auteurs qui ont écrit des livres publiés après 2000.
# Obtenir les livres qui ne sont pas des best-sellers et dont le classement est compris entre 3 et 7.
# Récupérer la liste des auteurs qui n'ont pas écrit de livres.
# Trouver les livres qui ont été publiés entre 2010 et 2020 et qui sont des best-sellers.
# Obtenir les auteurs qui ont écrit au moins deux livres.
# Récupérer la liste des livres écrits par des auteurs dont le nom contient "Smith" et qui ont un classement supérieur à 6.
   