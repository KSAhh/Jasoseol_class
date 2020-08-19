from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def create(request):
    # 작성자 이름 설정하기
    # print(request.user)         # 터미널에서 현재 로그인 된 user확인

    if request.method == "POST":
        filled_form = JssForm(request.POST) # POST방식으로 전해져 온 데이터가 자기소개서 폼에 저장
        if filled_form.is_valid(): # 유효성 검증
            temp_form = filled_form.save(commit=False) # 데이터 기반으로 자기소개서 란 생성
            temp_form.author = request.user
            temp_form.save()
            return redirect('index') #render와는 세 번째 인자에 데이터를 넘겨줄 수 있지만, redirect는 index페이지로 보내주기만 함
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form} )

def detail(request, jss_id):
    try:
        my_jss = Jasoseol.objects.get(pk=jss_id)
    except:
        raise Http404

    # object가 없었을때, 404를 출력하는 함수
    # my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    return render(request, 'detail.html', {'my_jss':my_jss})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')
    
# model form을 이용한 update
def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss) #instance는 해당 object 위에 씌우는 것
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'jss_form':jss_form})