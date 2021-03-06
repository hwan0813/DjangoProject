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
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import InsertBook, DisplayMyPage, DisplayBook


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^mypage/', DisplayMyPage), #url에 mypage 요청들어오면 Dis~ 실행
    url(r'^insert/(?P<isbn>.+);(?P<title>.+);(?P<memo>.*)',
        InsertBook),
    #isbn이 링크뒤에 붙으면 바로 displaybook 이거 함수호출
    url(r'^show/(?P<isbn>.+)', DisplayBook),
]
