from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 자동으로 모델가져와서 폼형식으로 채워줌. 여기 밑에 채우는 형식대로 입력창생김. 
        fields = ['title', 'content','user_agent']
        widgets ={
            'user_agent' : forms.HiddenInput,
        }

    #title = forms.CharField(validators=[min_length_3_validator])
    #content = forms.CharField(widget=forms.Textarea)


    '''
    def save(self, commit = True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    ''' 