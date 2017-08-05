# blog/ urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^insert/(?P<isbn>.+);(?P<title>.+);(?P<memo>.*)', 
    views.InsertBook), # 왜 사이트는 MyAppView라고햇찌 ㅅㅂ
    
    url(r'^$', views.post_list),
   
     # 꺽쇠가 문자열의 시작, 달러가 문자열의 끝
     url(r'^new/$', views.post_new),
     url(r'^(?P<id>\d+)/edit/$', views.post_edit),
]
# views.post_list를 호출하겠다 ()인 함수를 호출한게아니라 함수 자체를 넘겨줌

