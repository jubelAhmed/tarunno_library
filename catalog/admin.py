from django.contrib import admin
from .models import Author,Language,Genre,Book,BookInstance
# Register your models here.

# Header and title change
admin.site.site_header = 'Tarunno Public Library' 
admin.site.site_title = 'Public Library' 
admin.site.index_title = 'Library Admin Portal' 


from django.db.models import Value
from django.db.models.functions import Concat


class BooksInline(admin.TabularInline):
    model = Book.author.through
    # this for many to many relation inline system  
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','show_all_books','date_of_birth','date_of_death')
    list_display_links = ('full_name', 'date_of_birth')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    search_fields = ('first_name','last_name')
    inlines = [BooksInline]

    def full_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'  
    full_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')
    
    full_name.short_description = 'Full Name'
    
    # list_filter = ('first_name','date_of_birth')
    # inlines = [BooksInline]
    
    

admin.site.register(Language)
admin.site.register(Genre)

class BooksInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','show_author','summery','display_genre')
    search_fields = ('title','author__first_name')
    inlines = [BooksInstanceInline]
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin): 
    list_display = ('book','borrower','book_borrow_date','due_back')
    list_filter = ('status','due_back')
    
    fieldsets = (
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back')
        })
    )
    



