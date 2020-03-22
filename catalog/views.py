from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# default 
from datetime import date,timedelta
from django.views.generic import ListView,DetailView

#custom
from .models import Book,BookInstance,Author,Genre

start_date = date.today()
end_date_week_difference = start_date + timedelta(days=6)

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_book_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    all_books = Book.objects.order_by('-book_added_date')[:6]
    
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_book_instance_available':num_book_instance_available,
        'num_authors':num_authors,
        'num_genres':num_genres,
        'all_books':all_books,
    }
    
    return render(request,'index.html',context=context)


class BookListView(ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'books/book_list.html'
    paginate_by = 8
    
    def get_queryset(self):
        return Book.objects.order_by('-book_added_date')[:6]
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['authors'] = 'This is just some data'
        return context
    
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    

class AuthorListView(ListView):
     model = Author
     template_name = 'books/author_list.html'
     context_object_name = 'author_list'
     
     def get_queryset(self):
          return Author.objects.order_by('first_name')
    

from django.shortcuts import get_object_or_404

def author_detail_view(request,pk):
    author= get_object_or_404(Author,pk=pk)
    return render(request,'books/author_detail.html',context={'author':author})
    
    
