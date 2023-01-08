import re
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse
from django.template import context
from .models import Massage
from django.db.models import Q
import json
from landingpage.models import User
from .forms import MessageForm
from landingpage.models import *
# Create your views here.

def chatting(request, pk:int):
    chat_partner = get_object_or_404(User, pk=pk)
    message = Massage.objects.filter(
        Q(receiver=chat_partner, sender=request.user) | Q(receiver=request.user, sender= chat_partner)
    )
    message.update(seen=True)
    
    context = {
        "chat_partner": chat_partner,
        "message": message,
    }

    return render(request, "chatroom.html",context)

def listUser(request):
    comp_user =  User_company.objects.all()
    eo_user = User_EO.objects.all()

    context = {
        'comp_user' : comp_user,
        'eo_user' : eo_user,
    }

    return render(request, 'listchat.html', context)



def ajax_load_massage(request,pk):
    chat_partner = get_object_or_404(User, pk=pk)
    messages = Massage.objects.filter(seen=False)


def chat(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient = User.objects.get(username=form.cleaned_data['recipient'])
            Massage.objects.create(
                sender=request.user,
                recipient=recipient,
                message=form.cleaned_data['message']
            )
            form = MessageForm()
    else:
        form = MessageForm()
    messages = Massage.objects.filter(sender=request.user)
    return render(request, 'chat.html', {'form': form, 'messages': messages})