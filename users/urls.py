
from django.urls import path
from .views import UserList, UserLogin,set_csrf_token,UserTest

urlpatterns = [
   path('',UserList.as_view()),
   path('login/',UserLogin.as_view()),
   path('set-csrf/', set_csrf_token, name='Set-CSRF'),
   path('test/', UserTest.as_view(), name='test'),


   # path('',views.get_user)
]