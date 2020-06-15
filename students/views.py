from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import User


# Create your views here.

def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        count = User.objects.filter(email=email, password=password).count()
        if count > 0 :
            return HttpResponse("You are authenticated successfully ...")
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