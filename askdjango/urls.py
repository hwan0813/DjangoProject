"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import InsertBook, DisplayMyPage, DisplayBook
from crawl.views import DisplayLotte
from django.shortcuts import redirect

#최상위주소로 들어오면 바로 메인페이지로 연결해주고싶을때
def root(request):
    return redirect('dojo:post_list2')

urlpatterns = [
    #url(r'^$',root, name ='root'),
    url(r'^$', lambda r:redirect('dojo:post_list2'), name ='root'),
    # 람다함수로 바로 써도됨. 람다람다 . 
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^mypage/', DisplayMyPage), #url에 mypage 요청들어오면 Dis~ 실행
    url(r'^insert/(?P<isbn>.+);(?P<title>.+);(?P<memo>.*)',
        InsertBook),
    #isbn이 링크뒤에 붙으면 바로 displaybook 이거 함수호출
    url(r'^show/(?P<isbn>.+)', DisplayBook),
    url(r'^dojo/',include('dojo.urls', namespace ='dojo')), # 절대로 url(r'^dojo/$'  달러쓰면안됨. 인클루드할땐. 
    # namespace를 인클루드의 인자로 넣는이유: 그 뷰 참조할때 중복피하기위해. 이러헥하면 dojo:post_list2 이렇게 특정지정 가능. 
    url(r'^accounts/',include('accounts.urls')),
    
]
# 디버그 툴바 띄워주기. 실제 서비스모드에서는 셋팅에서 DEBUG=False 임. 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ 
         url(r'^__debug__/', include(debug_toolbar.urls)),
    ]