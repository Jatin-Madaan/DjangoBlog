from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import *


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
            request.session['user_id'] = User.objects.values('id').filter(email=email, password=password)[0]['id']
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
        data = Blog.objects.all()
        context = {
            'data' : data
        }
        return render(request, 'studentbook/home.html', context)
    return redirect('login')

def logout(request):
    del request.session['is_logged']
    return redirect('login')

def create_post(request):
    if request.POST:
        good_name = request.POST['good_name']
        description = request.POST['description']
        title = request.POST['title']
        image = request.POST['image']
        user_id = request.session['user_id']

        obj = Blog(good_name=good_name, description=description, title=title, image=image)
        obj.user_id_id = user_id
        obj.save()
        messages.success(request, 'Your Post has been added')
        return redirect('home')
    return render(request, 'studentbook/create_post.html')

def readmore(request, id):
    data = Blog.objects.get(id=id)
    context = {
        'data' : data
    }
    return render(request, 'studentbook/readmore.html', context)