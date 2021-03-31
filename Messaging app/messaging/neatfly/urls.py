from django.urls import path, include
from django.http import HttpResponseRedirect
from . import views
def root(request):
    return HttpResponseRedirect("/home")
urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.signup_view, name="signup")
]
