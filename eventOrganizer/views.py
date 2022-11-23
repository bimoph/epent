from django.shortcuts import render

# Create your views here.
def event_profile(request):
    context = {}
    return render(request,"event_profile.html", context)