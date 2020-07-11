from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import add_task

def main(request):
    task_sent=add_task.objects.all()
    return render(request,'main_frame.html',{'task_sent':task_sent})

def form(request):
    if request.method=='POST':
        i=request.POST['id']
        t=request.POST['task']
        d=request.POST['description']
        dt=request.POST['date']

        database=add_task(id=i,task=t,description=d,dateTime=dt)
        database.save()

        task_sent = add_task.objects.all()
        return render(request,'main_frame.html',{'task_sent':task_sent})

    else:
        return render(request, 'form.html')


def delete(request,id):
    print(id)
    data=add_task.objects.get(id=id)
    data.delete()

    return redirect(main)
