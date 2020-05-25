from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Task
from django.http import HttpResponse,HttpResponseRedirect
from .forms import TaskForm,TaskUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages

@login_required
def home(request,pk):

    
    user  = User.objects.get(id=pk)
    tasks = user.task_set.all()
    tasks = tasks[::-1]
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=user)
        
        if form.is_valid():
            user.task_set.create(name=request.POST.get('name'))
            return HttpResponseRedirect(request.path_info)
            
    context = {
        'user':user,
        'tasks':tasks,
        'form':form
    }
    
    if request.user.id != user.id :
        return redirect(f'/{request.user.id}')

    return render(request,'todo/home.html',context)


@login_required

def update_task(request,pk,task_id):
    user = request.user
    print(user)
    print(task_id)
    task = user.task_set.all().get(id=task_id)
    
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect(f'/{user.id}')
    context={
        'tasks':task,
        'form':form
    }
    return render(request,'todo/update.html',context)

@login_required

def delete_task(request,pk,task_id):
    user = request.user
    task = user.task_set.all().get(id=task_id)
   
    if request.method == 'POST':
        task.delete()
        return redirect(f'/{user.id}')
    return render(request,'todo/delete.html',{'task':task})


@login_required

def delete_all_tasks(request,pk):
    user = request.user
    tasks = user.task_set.all()
    task_count = tasks.count()

    if request.method == 'POST':
        for task in tasks:
            task.delete()
        return redirect(f'/{user.id}')
    return render(request,'todo/delete_all.html',{'task_count':task_count})




def register_page(request):
    if request.user.is_authenticated:
        return redirect(f'/{request.user.id}')
    else:
        form = TaskUserForm()
        if request.method == 'POST':
            form = TaskUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                # messages.success(request,'Account was created for '+username)
                
                return redirect('login')
        return render(request,'todo/register.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.user.is_authenticated:
        return redirect(f'/{request.user.id}')
    else:
        user = request.user
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username=request.POST.get('username')
                password=request.POST.get('password')
                user = authenticate(username=username,password=password)
                user.id = user.id
                print('user view',user.id)
                if user is not None:
                    login(request,user)
                    return redirect(f'/{user.id}')
        else:
            form = AuthenticationForm()
        context = {'form':form}
        return render(request,'todo/login_user.html',context)

def contact(request):
    return render(request,'todo/contact.html')


def about(request):
    return render(request,'todo/about.html')


def delete_account(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('login')
    return render(request,'todo/delete_account.html')
    
    