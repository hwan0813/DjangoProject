from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300) # 크기존나 크게하니까 됨. 중요한건 바꾸고서 makemigrations랑 migrate까지 해줘야한다는사실 .

    def __str__(self):
        return self.title

class Lotte(models.Model):
    pro_name = models.CharField(max_length=200)
    price = models.CharField(max_length=300) # 크기존나 크게하니까 됨. 중요한건 바꾸고서 makemigrations랑 migrate까지 해줘야한다는사실 .
    
    def __str__(self):
        return self.pro_name