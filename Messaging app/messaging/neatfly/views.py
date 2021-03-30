from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "neatfly/index.html")


def login_view(request):
    if request.method == "GET":
        return render(request, "neatfly/login.html")
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