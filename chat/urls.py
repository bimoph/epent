from xml.etree.ElementInclude import include
from django.urls import path
from chat.views import *

app_name = "chat"

urlpatterns = [
    path('<int:pk>/', chatting, name="chatting"),
    path('room/', listUser, name="listUser"),
    
]
