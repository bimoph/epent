from django.shortcuts import render
from .forms import LengkapiForm
from django.shortcuts import redirect
from landingpage.models import Event
# Create your views here.
def event_home(request):
    user = request.user
    context = {
        'user': user.username
    }
    return render(request,"event_home.html", context)

def event_profile(request):
    # user = request.user
    try:
        data_event = Event.objects.get(user=request.user)
    except:
        data_event = False
    if not data_event: # jika query set kosong
        data_event = False
    print(data_event)
    context = {
        'data_event': data_event, 
    }
    return render(request, "event_profile.html", context)

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