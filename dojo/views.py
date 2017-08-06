# dojo 밑의 view.py 파일.
import os
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect ,render ,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages

def mysum2(request,numbers):
    result = sum(map(lambda s : int(s or 0), numbers.split("/")))
    # 스플릿하고, map으로 모두 int로 바꿔줌. 
    # 그다음 다 더해주고 리턴. 
    # 람다식을 추가해줬는데 이건, 슬래쉬가 // 두번들어갈경우 스플릿하면 빈문자열이 나오는데
    # 이 빈문자열은 int로 바꾸어주지 못한다 그래서 오류발생
    # 그래서 lambda식을 이용해서 or! 를 이용해서 거짓->이면 0으로 써라 라고 지정해준것. 
    return HttpResponse(result)
def mysum(request, x, y=0, z=0): # 디폴트 인자를 지정. 그니까 안넘어와도 디폴트값이 자동으로 되는거 .씹굿. 
    # request: HTTPRequest 

    return HttpResponse(int(x) + int(y) + int(z)) # httpResponse 임포트 해주고 써야함. 
# HttpResponse(x+100)으로 하면 안되는 이유는 x는 무조건 문자열이기 때문. 
# 그래서 x를 int 로 바꿔주고 하면 되네 . 

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {} 살이시네요 '.format(name, age))

# 그냥 바로 html 코드를 응답하는것. 
def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>하이 루</h1>
    <p>{name}</p>
    <p> 실습중 <p>
    '''.format(name = name)
    )

def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request,'새 포스팅을 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', { 
            'form':form,   
        })

#수정하기 추가 
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save()
            messages.success(request,'포스팅을 수정했습니다')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', { 
            'form':form,   
        })

# 메인화면. 데이터베이스에서 가져와서 보여주는것 추가. 
# pylint: disable=E1101
def post_list2(request):
    qs = Post.objects.all()
    
    q = request.GET.get('q','') # q있으면 ㄴ가져오고 없으면 빈문자가져오고
    if q: # q가 있다면...?
        qs = qs.filter(title__icontains = q)
    #이게 가능한 이유가 그냥 request라는 인자때문에 그냥 무한히 왕복 주고받고가능한건가. 

    name = ' 이것도 넘겨보자. '
    return render(request, 'dojo/post_list2.html',
     {'name':name, 'post_list' : qs, 'q':q} 
    ) # 인자 넘기나봄. 

def post_detail(request, id):
    #try: # 포스트가 삭제되었을경우, 서버에러(500)으로 처리되는것이아니라 404로 처리도되도록 예외처리해줌. 
    #    post = Post.objects.get(id=id)
    #except Post.DoesNotExist:
    #    raise Http404
    # 위의 4줄이랑 같은코드. 이걸쓰자. shortcut으로부터 import는 하고 
    post = get_object_or_404(Post, id=id)
    #지정레코드가 없는것은 서버오류가 아니므로 모든 인스턴스처리는 get_ob~404로 한다. 

    return render(request, 'dojo/post_detail.html', {
    'post':post,
    })


#각함수는 두줄씩띄워주는게 좋다
def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬 장고',
        'items': ['파썬','장고','Celery','Azure','AWS'],
    }, json_dumps_params = {'ensure_ascii': False}) 

# 파일 다운로드하게하는 코드임. 
def excel_download(request):
    filepath = '/home/jeongseunghwan/django/DjangoProject/aa.xlsx'
    filename = os.path.basename(filepath) #os 임포트해야함.
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename ="{}"'.format(filename)
        return response

