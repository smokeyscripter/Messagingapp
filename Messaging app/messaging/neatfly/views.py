from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
from .util import hash
def index(request):
    return render(request, "neatfly/index.html")


def login_view(request):
    if request.method == "GET":
        return render(request, "neatfly/login_view.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "neatfly/login.html", {
                "message": "Invalid username and/or password."
            })


def signup_view(request):
    if request.method == "POST":
        pfp = request.FILES["picture"]
        name = hash(pfp.name[:len(pfp.name)-4]) + pfp.name[len(pfp.name)-4:]
        fs = FileSystemStorage()
        name = fs.save(name, pfp)
        url = fs.url(name)
        print(url)
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        print(password1)
        is_secure = True #for now
        email = request.POST["email"]
        user = User.objects.create_user(username=username, email=email, password=password1, picture=url)
        if not is_secure:
            return HttpResponse({
                "message": "Your password is not secure enough."
            })
        return HttpResponse(user.picture)
    elif request.method == "GET":
        return render(request, "neatfly/signup_view.html")

def validate(password):
    pass
