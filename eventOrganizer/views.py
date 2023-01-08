from django.shortcuts import render
from .forms import LengkapiForm
from django.shortcuts import redirect

# Create your views here.
def event_home(request):
    context = {}
    return render(request,"event_home.html", context)

def event_profile(request):
    return render(request, "event_profile.html", {})

def event_lengkapi_profile(request):
    if request.method == 'POST':
        form = LengkapiForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('eventOrganizer:event_profile')
    else:
        form = LengkapiForm()
    return render(request, 'event_lengkapi_profile.html', {'form': form})