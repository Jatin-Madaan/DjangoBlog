from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import User


# Create your views here.

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('home')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        count = User.objects.filter(email=email, password=password).count()
        if count > 0 :
            request.session['is_logged'] = True
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'studentbook/login.html')


def signup(request):
    context = {}
    return render(request, 'studentbook/signup.html',context)

def register_user(request):

    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        obj = User(username=username, password = password, email = email)
        obj.save()
        messages.success(request, 'You are registered successfully .. ')
        return redirect('login')

def home(request):
    if request.session.has_key('is_logged'):
        return render(request, 'studentbook/home.html')
    return redirect('login')

def logout(request):
    del request.session['is_logged']
    return redirect('login')