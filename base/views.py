from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from .PhoneBackEnd import PhoneBackEnd
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    print(user)
    return render(request, 'app/index.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        print(request.POST.get('password'))
        user = PhoneBackEnd.authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')


def signin(request):
    return render(request, 'app/auth/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def sample_test(request):
    if request.method == "POST":
        pass
    else:

        return render(request, 'app/sample_test.html')
    
def farmers(request):
    if request.method == "POST":
        pass
    else:

        return render(request, 'app/farmers.html')

def users(request):
    if request.method == "POST":
        pass
    else:

        return render(request, 'app/users.html')