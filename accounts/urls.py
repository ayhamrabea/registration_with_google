from django.urls import path , include
from . import views
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserLoginForm
from .views import RegesterView



urlpatterns = [
    path('',views.index,name='home'),
    path('login/',LoginView.as_view(authentication_form=UserLoginForm),name='login'),
    path('logout/', views.log_out, name='log_out'),
    # path('profile/', edit_profile, name='profile'),
    path('singup',RegesterView.as_view(), name='singup'),
    
    path('',include('django.contrib.auth.urls'))
]
