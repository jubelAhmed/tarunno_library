from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200,help_text="Enter a book genre(e.g. Science Fiction)")
    
    def __str__(self):
        return self.name 



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    class Meta:
        ordering=['last_name','first_name']
    
    def get_absolute_url(self):
        return reverse('author_detail',args=[str(self.id)])
    
    def show_all_books(self):
        return ', '.join(book.title for book in self.book_set.all())
    # self.book_set.all() ///  book is Model name ,, book_set in geting value for many to many relation which relation declare from another Model
    
    
    def __str__(self):
        return f'{self.first_name},{self.last_name}'
       

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    summery = models.TextField(help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,help_text='Select a genre for this book')
    
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
    def show_author(self):
        return ', '.join(author.first_name for author in self.author.all()[:3])
    show_author.short_description = 'Author'
    
    def __str__(self):
        return f'{self.title}'


from datetime import date

from django.contrib.auth.models import User

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique Id for this particular book for whole library')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    book_borrow_date = models.DateTimeField(auto_now_add=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today()> due_back:
            return True
        return False
        
     
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved')
    )
    
    
    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank= True,
        default= 'm',
        help_text='Book Availability'
        
    )
    
    class Meta:
        ordering=['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    
    def __str__(self):
        return f'{self.id} ({self.book.title})'  


class Language(models.Model):
    language_name = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.language_name}'