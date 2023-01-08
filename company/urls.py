
from django.urls import path
from company.views import *

app_name = "company"

urlpatterns = [
    path('', company_home, name='company_home'),
    path('company_profile/', company_profile, name='company_profile'),
    path('company_lengkapi_profile/', company_lengkapi_profile, name='company_lengkapi_profile'),

]



