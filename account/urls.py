from django.contrib import admin
from django.urls import path
from .import views

from account.views import user_login,user_logout

urlpatterns = [
   path('',views.ask,name="ask"),
   path('signup/',views.signup,name="signup"),
    path('signin/',user_login,name="login"),
    path('main_frame/logout',user_logout,name="logout"),
]
