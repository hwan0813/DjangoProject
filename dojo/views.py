# dojo 밑의 view.py 파일.
from django.http import HttpResponse
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