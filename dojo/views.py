# dojo 밑의 view.py 파일.
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, x, y=0, z=0): # 디폴트 인자를 지정. 그니까 안넘어와도 디폴트값이 자동으로 되는거 .씹굿. 
    # request: HTTPRequest 

    return HttpResponse(int(x) + int(y) + int(z)) # httpResponse 임포트 해주고 써야함. 
# HttpResponse(x+100)으로 하면 안되는 이유는 x는 무조건 문자열이기 때문. 
# 그래서 x를 int 로 바꿔주고 하면 되네 . 