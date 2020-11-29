from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm 

# Create your views here.

def register(request):
    if request.method== 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')  
        else:
            return render(request, 'accounts/register.html',{'form':form})
    else:
        form = CreateUserForm()
        return render(request, 'accounts/register.html',{'form':form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            return render(request,'accounts/login.html',{})
       
    else:
        return render(request, 'accounts/login.html',{})
    
@login_required(login_url="/login/")
def home(request):
    return render(request,'home.html')



