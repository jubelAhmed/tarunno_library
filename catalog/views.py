from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book,BookInstance,Author,Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_book_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_book_instance_available':num_book_instance_available,
        'num_authors':num_authors,
        'num_genres':num_genres
    }
    
    return render(request,'index.html',context=context)