from django.http import HttpResponse, JsonResponse
from django.views.generic import View,TemplateView

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