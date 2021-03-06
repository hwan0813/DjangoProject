from django.conf.urls import url # url 패턴 쓰기위해 임포트
from . import views
from . import views_cbv

urlpatterns = [
    
    #존나 많이 / 슬래쉬 숫자 받아도 다 더할수있도록
    url(r'^sum/(?P<numbers>[\d/]+)$',views.mysum2), # 정규표현식을 느슨하게.. / 도 표현되도록?

    url(r'^sum/(?P<x>\d+)/$', views.mysum) , 
    # 만약 여기서 $를 써주지않으면 그냥 무조건 주소중에 숫자 하나만! 들어오면 바로 이게 실행됨. 즉 숫자 두개 100/200 이렇게들어오는것도
    # 다 첫번째 url패턴에서 처리하는것. 원래는 다음으로 넘어가야되는데 .
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum) ,
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum), 
    
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    # views를 임포트해야 쓸수있음. 
    # dojo 나오고, sum 나오고 숫자!! 나오면 view.mysum이 호출된다는 말. 
    url(r'^$',views_cbv.post_list, name='post_list'),
    url(r'^list1/$',views.post_list1),
    url(r'^list2/$',views.post_list2, name='post_list2'), # URL Reverse를 위한 지정. 
    url(r'^list3/$',views.post_list3),
    url(r'^excel/$',views.excel_download),

    url(r'^cbv/list1/$',views_cbv.post_list1),
    url(r'^cbv/list2/$',views_cbv.post_list2),
    #url(r'^cbv/list3/$',views_cbv.post_list3),
    #url(r'^cbv/excel/$',views_cbv.excel_download),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name = 'post_detail'),
    # url 막바꿔도 이제 url reverse때매 알아서 하이퍼링크바뀐주소가 잘 찾아서감. 
    url(r'^new/$', views.post_new, name ='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name = 'post_edit'),

    url(r'^cbv/new/$', views_cbv.post_new),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete),
    url(r'^comments/$', views.comment_list, name = 'comment_list'),

]