from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)


    
    # 자소서 form custom
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # super: class 즉, ModelForm에 있는 것들을 가져와서 쓸 수 있다.
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({# title: 원하는 필드로 title을 가져옴
            'class': 'jss_title',
            'placeholder': '제목',
        }) 