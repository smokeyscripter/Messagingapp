from django.urls import path, include
from django.http import HttpResponseRedirect
from neatfly.views import signup
from neatfly.views import home
from neatfly.views import login
def root(request):
    return HttpResponseRedirect("/home")
urlpatterns = [
    path("", root),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
   
]