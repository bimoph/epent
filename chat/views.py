import re
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse
from django.template import context
from .models import Massage
from landingpage.models import User_company, User_EO, User
from django.db.models import Q
import json
# Create your views here.

def chatting(request, pk:int):
    chat_partner = get_object_or_404(User, pk=pk)
    massage = Massage.object.filter(
        Q(receiver=chat_partner, sender=request.user) | Q(receiver=request.user, sender= chat_partner)
    )
    massage.update(seen=True)
    
    context = {
        "chat_partner": chat_partner,
        "massage": massage,
    }

    return render(request, "chatfeature.html",context)
