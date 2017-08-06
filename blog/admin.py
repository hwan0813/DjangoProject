from django.contrib import admin  #ㅇ걸해줘야 밑에 admin이되네
from blog.models import Book
from .models import Post,GameUser


admin.site.register(Book)
admin.site.register(Post)

admin.site.register(GameUser) 