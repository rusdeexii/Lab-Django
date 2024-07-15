from django.contrib import admin

# Register your models here.

from helloworld.models import Author, Post, Contact

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Contact)
