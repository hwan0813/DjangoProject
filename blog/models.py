from django.db import models
from jsonfield import JSONField
from django import forms
from django.core.validators import MinLengthValidator
# Create your models here.
 
class Book(models.Model):
    isbn = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    memo = JSONField(default={}, dump_kwargs={'ensure_ascii': False})
    
    def __str__(self):
        return self.title

#forms 에서 model.py로 옮겨옴
def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    user_agent= models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                    choices=(
                                        ('A','A서버'),
                                        ('B','B서버'),
                                        ('C','C서버'),
                                    ))
    user_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    # 이렇게하면 서버네임과 유저네임이 묶여서 중복이 안되게됨.
    # 즉 무슨말이나면 A서버의 d와 B서버의 d는 별개로 존재가능함. 
    class Meta:
        unique_together =[
            ('server_name','user_name')
        ]