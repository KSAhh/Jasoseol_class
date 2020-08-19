from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
     # 첫 번째 인자 : 연결하고싶은 모델
     # object가 지워지면 어떻게 할 것인지. 연결된 자소설 오브젝튿도 지워짐