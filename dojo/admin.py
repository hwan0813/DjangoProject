from django.contrib import admin
from django.utils.safestring import mark_safe # 태그문자열을 문자처럼 되도록. 
from .models import Post, Comment

#그냥 단순 등록이아니라 이렇게 하면 admin 계정에서 웹으로 관리할때 내용이 상세하게 보임. 
@admin.register(Post) #장식자 형태로 쓴것. ... 까먹음. 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','status','content_size' ,'created_at', 'updated_at'
    ]
    actions = ['make_published','make_draft'] # 이렇게 액션 등록해야 만든 액션이 등록됨. 

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수' # 어드민관리하는쪽에 '글자수'로 보이게됨.
    #content_size.allow_tags = True # 이거쓰면 저기 <strong>태그가 적용됨. ->deprecated된기능임. 이제 마크세이프씀
    
    def make_published(self, request, queryset): #어드민에서 액션을 만드는 과정.
    # 리퀘스트와 쿼리셋이 잇어야 하며 이 액션은 status를 published로 바꾸기위한 작업. 하나하나 변경하는 것이 아니라
    # 한번에 체크리스트를 체크하고 한번에 바꾸기위한 작업. 
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 퍼블리쉬드로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 published로 변경'


    def make_draft(self, request, queryset): 
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 draft 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 draft로 변경'


# admin.site.register(Post, PostAdmin)# 어드민에 등록. 제일 기본적인 등록법. 

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    pass
