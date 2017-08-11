from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

# 장고에서 기본제공하는 UserCreationForm상속받아서
# 커스터마이징하는 과정. 
class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    #phone_number나 address는 기존의 User
    #creation폼에 없으므로 따로 저장구현해줘야함
    # pylint: disable=E1101
    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'])
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer',None)
        if answer != 6:
            raise forms.ValidationError('mismatched!')
        return answer