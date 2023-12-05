from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    biography = models.TextField(blank=True, null=True, verbose_name= "Biographie")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Date de naissance")

    def __str__(self):
        return self.name 


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    # slug = models.SlugField(max_length=255, blank=True)
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

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

   





 