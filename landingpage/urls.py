
from django.urls import path
from landingpage.views import show_login
from landingpage.views import show_signup1
from landingpage.views import show_signup2
from landingpage.views import show_landingpage

app_name = "landingpage"

urlpatterns = [
    path('', show_landingpage, name='landingpage'),
    path('login', show_login, name='login'),
    path('signup1', show_signup1, name='signup1'),
    path('signup2', show_signup2, name='signup2')
]



