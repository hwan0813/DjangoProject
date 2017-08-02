#accounts/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # 원투원이므로 하나만 지정됨. 한명의유저는 무조건 하나의 프로필만. 
    #user = models.OneToOneField(User) #FIXME: BAD CASE
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
