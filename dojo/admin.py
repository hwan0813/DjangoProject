from django.contrib import admin
from .models import Post

#그냥 단순 등록이아니라 이렇게 하면 admin 계정에서 웹으로 관리할때 내용이 상세하게 보임. 
@admin.register(Post) #장식자 형태로 쓴것. ... 까먹음. 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at'
    ]

# admin.site.register(Post, PostAdmin)#어드민에 등록. 
