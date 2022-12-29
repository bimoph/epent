from xml.etree.ElementInclude import include
from django.urls import path
from chat.views import *

app_name = "chat"

urlpatterns = [
    path('', chatting, name="chatting")
]
