# dojo/models.py
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,
        choices = (
            ('제목1', '제목1 레이블'), # ('저장된값','UI에 보여질레이블')
            ('제목2', '제목2 레이블'),
            ('제목3', '제목3 레이블'),
        ))
    #길이 제한이 있는 문자열 -> 캐릭터필드
    content = models.TextField(verbose_name="내용" , 
        help_text='여기에 내용을 입력하세요!') #verbose네임하면 필드입력이 이렇게 보여짐
        #help 텍스트하면 입력폼위에 회색글씨 작은걸로 도움말.
    #길이 제한이 없는 문자열 -> 텍스트필드, 데이터베이스는 엄연히 다르니까. 
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간,. 오토나우애드 =>
    # 현재 하나의 포스트 레코드가 최초저장될때 일시가 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해동레코드가 갱신될때마다 일시가 자동 저장.

