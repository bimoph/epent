
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

def register_eo2(request):
    form = EOForm()
    if request.method == "POST":
        form = EOForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('landingpage:login')

    context = {'form': form}
    return render(request, 'register_eo1.html', context)

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