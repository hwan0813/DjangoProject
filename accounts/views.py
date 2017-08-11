from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default: "accounts/login/"
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })

#이 장식자는 아직 로그인안했는데 프로필을 보려고하면 굳이 화면에 띄워줄필요 x
#그럴때 로그인을 강제하는 코드. 프로필 누르면 로그인화면으로 이동. 로그인성공시 프로필보여줌. 
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')