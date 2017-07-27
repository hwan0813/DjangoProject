from django import forms

from .models import Lotte

class PostForm(Forms.ModelForm):

    class Meta:
        model = Post
        field = ('pro_name','price',)
