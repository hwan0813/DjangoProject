from django.http import HttpResponse, JsonResponse
from django.views.generic import View,TemplateView , ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post

post_delete = DeleteView.as_view(model=Post, success_url = '/dojo/')
post_new = CreateView.as_view(model=Post)
post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)
# 글다쓰고 자동으로 이동하는 페이지는 원래는 success_url 인자로 지정해주지만
# 만약 안써도 현재 참조하는 모델에 get_absolute_url이 있으면 그 곳으로 이동한다.
post_list = ListView.as_view(model=Post, paginate_by=10)

class PostListView1(View):
    
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name = name)
        return HttpResponse(html)
    
    #클래스 기반 뷰이기때문에 이런 코딩이 가능한것. 
    def get_template_string(self):
        return '''
            <h1>하이 루</h1>
            <p>{name}</p>
            <p> 실습중 <p>
        '''

#이게 호출 받는 부분 인가봄. 클래스 기반 뷰에서. 
post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'

    # 별 설명안햇는데 클래스 기반뷰에서 넘길때 이렇게 하나봄. 
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass