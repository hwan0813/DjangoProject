from django.contrib import admin
from django.utils.safestring import mark_safe # 태그문자열을 문자처럼 되도록. 
from .models import Post

#그냥 단순 등록이아니라 이렇게 하면 admin 계정에서 웹으로 관리할때 내용이 상세하게 보임. 
@admin.register(Post) #장식자 형태로 쓴것. ... 까먹음. 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content_size' ,'created_at', 'updated_at'
    ]

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수' # 어드민관리하는쪽에 '글자수'로 보이게됨.
    #content_size.allow_tags = True # 이거쓰면 저기 <strong>태그가 적용됨. ->deprecated된기능임. 이제 마크세이프씀
    
# admin.site.register(Post, PostAdmin)#어드민에 등록.
