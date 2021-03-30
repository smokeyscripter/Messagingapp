from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.


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


def register_view(request):
    if request.method == "POST":
        pfp = request.FILES["picture"]
        fs = FileSystemStorage()
        name = fs.save(pfp.name, pfp)
        url = fs.url(name)
        print(url)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username=username, email=email, password=password, picture=url)
        except:
            return JsonResponse({
                "message": "error occurred while saving your profile"
            })
        return HttpResponse(user.picture)
    elif request.method == "GET":
        return render(request, "neatfly/signup_view.html")


