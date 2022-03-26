from asyncio import tasks
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
     
    context = {'tasks' : tasks,'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form':form}
    return render(request, 'tasks/updateTask.html', context)

def deleteFunc(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
   
    return redirect('/')
    

