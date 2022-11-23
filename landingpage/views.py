import datetime
from operator import imod
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
# from todolist.models import Task
# from todolist.forms import CreateTaskForm

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core import serializers

from django.http import JsonResponse
# Create your views here.
def show_landingpage(request):
    context = {}
    return render(request, "landing_page.html", context)

def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('eventOrganizer:event_profile'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            
            return response
            
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def show_signup1(request):
    context = {}
    return render(request,"signinp1.html", context)

def show_signup2(request):
    context = {}
    return render(request,"signinp2.html", context)