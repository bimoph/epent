
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
# from todolist.models import Task
from landingpage.forms import *

from django.shortcuts import redirect
from django.contrib.auth.forms import *
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
        if user is not None and user.is_EO:
            login(request, user) 
            return redirect('landingpage:register_eo2')
        elif user is not None and user.is_company:
            login(request, user) 
            return redirect('landingpage:register_company2')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            # if user.is_EO:
            #     return redirect('landingpage:register_eo2')
            # elif user.is_company:
            #     return redirect('landingpage:register_company2')
            return redirect('landingpage:login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def register_eo1(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat, silahkan lanjutkan pengisian data!')
            return redirect('landingpage:register_eo2')

    context = {'form': form}
    return render(request, 'register_eo1.html', context)

# @csrf_extempt
def register_eo2(request):
    # form = EOForm()
    if request.method == "POST":
        new_EO = User_EO(user=request.user, 
                        name_event=request.POST.get('nama_event'),
                        email= request.POST.get('email'))
        new_EO.save()
        return redirect('eventOrganizer:event_profile')
        # form = EOForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Akun telah berhasil dibuat!')
        #     return redirect('landingpage:login')

    context = {}
    return render(request, 'register_eo2.html', context)

def register_company1(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat, silahkan lanjutkan pengisian data!')
            return redirect('landingpage:register_company2')

    context = {'form': form}
    return render(request, 'register_eo1.html', context)

def register_company2(request):
    form = EOForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('landingpage:login')

    context = {'form': form}
    return render(request, 'register_eo1.html', context)

def logout_user(request):
    logout(request)
    return redirect('landingpage:landingpage')