from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    context = {}
    return render(request, 'studentbook/login.html', context)


def signup(request):
    context = {}
    return render(request, 'studentbook/signup.html',context)