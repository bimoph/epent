from django.shortcuts import render

# Create your views here.
def show_landingpage(request):
    context = {}
    return render(request, "landing_page.html", context)

def show_login(request):
    context = {}
    return render(request,"login.html", context)

def show_signup1(request):
    context = {}
    return render(request,"signinp1.html", context)

def show_signup2(request):
    context = {}
    return render(request,"signinp2.html", context)