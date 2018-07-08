from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import uuid
from datetime import date
import os


# Create your models here.
class GenerModel(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class LanguageModel(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BookModel(models.Model):
    title =models.CharField(max_length=200)
    author= models.ForeignKey('AuthorModel' ,on_delete=models.CASCADE)
    summary =models.CharField(max_length=2000,help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(GenerModel, help_text='Select a genre for this book')
    language = models.ManyToManyField(LanguageModel, help_text='Select a languages for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('book-detail', args=[str(self.id)])

    def display_language(self):
        return ' , '.join([language.name for language in self.language.all()[:]])
    display_language.short_description = 'language'


    def display_genre(self):
        return ' , '.join([genre.name for genre in self.genre.all()[:]])
    display_genre.short_description = 'Gener'


class AuthorModel(models.Model):
    name = models.CharField(max_length=200)
    data_of_birth =models.DateTimeField(null=True , blank =True)
    date_of_death= models.DateTimeField(null=True ,blank=True)

    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-details' , args=[str(self.id)] )

class BookInstanceModel(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    id =models.UUIDField(primary_key=True ,default=uuid.uuid4)
    book =models.ForeignKey('BookModel',on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)
    def __str__(self):
        return self.status

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
