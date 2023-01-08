
from django.urls import path
from eventOrganizer.views import *

app_name = "eventOrganizer"

urlpatterns = [
    path('', event_home, name='event_home'),
    path('event_profile/', event_profile, name='event_profile'),
    path('event_lengkapi_profile/', event_lengkapi_profile, name='event_lengkapi_profile'),

]



