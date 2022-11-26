from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_landingpage(request):
    context = {}
    return render(request, "landing_page.html", context)

def show_login(request):
    context = {}
    return render(request,"login.html", context)

def show_signup1(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request,"signinp1.html", context)

def show_signup2(request):
    context = {}
    return render(request,"signinp2.html", context)