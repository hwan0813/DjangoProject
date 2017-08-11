from django.contrib.auth.forms import UserCreationForm

# 장고에서 기본제공하는 UserCreationForm상속받아서
# 커스터마이징하는 과정. 
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)