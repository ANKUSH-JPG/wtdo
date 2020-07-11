from django.contrib import admin
from django.urls import path,include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import  views

urlpatterns = [
    path('',views.main,name="main"),
    path('form',views.form,name="form"),
    path('delete/<int:id>',views.delete,name="delete"),

]

urlpatterns+=staticfiles_urlpatterns()