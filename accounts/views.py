from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # auth에 model폼이 들어있음
# Create your views here.

def signup(request):
    regi_form = UserCreationForm()          # model 폼
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index') 

    return render(request, 'signup.html', {'regi_form':regi_form})