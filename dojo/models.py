# dojo/models.py
import re
from django.conf import settings
from django.forms import ValidationError
from django.db import models

# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('invalid LngLat Type')

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class Post(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    #아래처럼 하면 화살표눌러서 기사, 스포츠, 등등에서 선택하게 해줌.
    #title = models.CharField(max_length=100,
    #    choices = (
    #        ('제목1', '기사'), # ('저장된값','UI에 보여질레이블')
    #        ('제목2', '스포츠'),
    #        ('제목3', '등등'),
    #    ))
    #길이 제한이 있는 문자열 -> 캐릭터필드
    content = models.TextField(verbose_name="내용" , 
        help_text='여기에 내용을 입력하세요!') #verbose네임하면 필드입력이 이렇게 보여짐
        #help 텍스트하면 입력폼위에 회색글씨 작은걸로 도움말. 
    #길이 제한이 없는 문자열 -> 텍스트필드, 데이터베이스는 엄연히 다르니까.
    
    tag_set = models.ManyToManyField('Tag', blank = True)
    #그냥 Tag하면 안되는이유가 Tag클래스가 이거보다 뒤에 정의되어있기때문. 그래서 이렇게하는거. 

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='경도/위도 포맷으로 입력',
         blank=True, validators=[lnglat_validator] ) # 블랭크 트루하면 값 안넣어도 ㅇㅋ.
         # validator 저렇게 지정해주는게 정규식 검사임. 
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간,. 오토나우애드 =>
    # 현재 하나의 포스트 레코드가 최초저장될때 일시가 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해동레코드가 갱신될때마다 일시가 자동 저장.

    class Meta: #기본 정렬 옵션 지정해주는것. id기준으로 역순 출력되도록. 
        ordering = ['-id']
        

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
