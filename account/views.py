from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout

def ask(request):
    return render(request,"ask.html")

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        form.save()
        return HttpResponseRedirect(reverse('login'))

    else:
        form=UserCreationForm()
        return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return HttpResponseRedirect(reverse('main'))
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

def user_logout(request):
    if request.method=="POST":
         logout(request)
         return HttpResponseRedirect(reverse('ask'))