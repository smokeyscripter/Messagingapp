from django.urls import path, include
from django.http import HttpResponseRedirect
from . import views
def root(request):
    return HttpResponseRedirect("/home")
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view),
    path("register/", views.register_view)
]
