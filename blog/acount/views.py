from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username} !!')
            return redirect('home')
    else:
        form = CreateUserForm()

    return render(request,'register.html',{'form' : form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')
