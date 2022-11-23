
from django.urls import path
from eventOrganizer.views import event_profile

app_name = "eventOrganizer"

urlpatterns = [
    path('', event_profile, name='event_profile'),
]



