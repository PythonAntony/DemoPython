from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import mytask
from  .forms import  TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.
class Tasklistview(ListView):
    model = mytask
    template_name = 'hometask1.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = mytask
    template_name ='detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = mytask
    template_name ='update.html'
    context_object_name = 'task'
    fields=('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = mytask
    template_name ='delete.html'
    success_url = reverse_lazy('todoapp:cbvhometask')



def add(request):
    task1 = mytask.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task=mytask(name=name, priority=priority, date=date)
        task.save()
    return render(request,'hometask.html',{'task1':task1})

def addtask(request):
    if request.method=="POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task=mytask(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request,'home.html')

def detail(request):
    task = mytask.objects.all()
    return render(request,'detail.html',{'task':task})
def delete(request, taskid):
    task=mytask.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=mytask.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f':f, 'task':task})