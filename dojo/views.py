# dojo 밑의 view.py 파일.
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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

def post_list2(request):
    name = ' 공ㅇ'
    return render(request, 'dojo/post_list2.html', {'name':name}) # 인자 넘기나봄. 

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