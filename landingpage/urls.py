
from django.urls import path
from landingpage.views import *

app_name = "landingpage"

urlpatterns = [
    path('', show_landingpage, name='landingpage'),
    # path('login', show_login, name='login'),
    # path('signup1', show_signup1, name='signup1'),
    # path('signup2', show_signup2, name='signup2'),
    path('register_eo1/', register_eo1, name='register_eo1'),
    path('register_eo2/', register_eo2, name='register_eo2'),
    path('register_company1/', register_company1, name='register_company1'),
    path('register_company2/', register_company2, name='register_company2'),


]



