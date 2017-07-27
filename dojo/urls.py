from django.conf.urls import url # url 패턴 쓰기위해 임포트
from . import views
urlpatterns = [
    url(r'^sum/(?P<x>\d+)/$', views.mysum) , 
    # 만약 여기서 $를 써주지않으면 그냥 무조건 주소중에 숫자 하나만! 들어오면 바로 이게 실행됨. 즉 숫자 두개 100/200 이렇게들어오는것도
    # 다 첫번째 url패턴에서 처리하는것. 원래는 다음으로 넘어가야되는데 .
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum) ,
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum) 
    # views를 임포트해야 쓸수있음. 
    # dojo 나오고, sum 나오고 숫자!! 나오면 view.mysum이 호출된다는 말. 
]