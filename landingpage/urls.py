
from django.urls import path
from landingpage.views import show_login
from landingpage.views import show_signup1
from landingpage.views import show_signup2

app_name = "landingpage"

urlpatterns = [
    path('login', show_login, name='show_todolist'),
    path('signup1', show_signup1, name='signup1'),
    path('signup2', show_signup2, name='signup2')
]



