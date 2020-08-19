from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # auth에 model폼이 들어있음
from django.contrib.auth.views import LoginView
# Create your views here.

def signup(request):
    regi_form = UserCreationForm()          # model 폼
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index') 

    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView):       #MyLoginview가 django의 내용을 다 담고있음
    templates_name = 'login_html'