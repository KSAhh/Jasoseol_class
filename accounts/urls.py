# template -> registration 폴더 생성하는 방식
# from django.urls import path
# from .views import signup
# from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     path('signup/', signup, name="signup"),    
#     path('login/', LoginView.as_view(), name="login"),
#     path('logout/', LogoutView.as_view(), name="logout"),
# ]

# ----------------------------------------------------------

# template -> registration 폴더가 아닌, django github에서 불러오는 방식
from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),    
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

