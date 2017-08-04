from django.contrib import admin  #ㅇ걸해줘야 밑에 admin이되네
from blog.models import Book
from .models import Post
admin.site.register(Book)
admin.site.register(Post)