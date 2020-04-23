
#from django.contrib import admin
#from .models import EBook # add this

#class BookAdmin(admin.ModelAdmin):  # add this
#     list_display = ('title', 'description', 'completed') # add this

    # Register your models here.
#admin.site.register(Book, BookAdmin) # add this
from django.contrib import admin
from .models import Category, Ebook, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Comment)
