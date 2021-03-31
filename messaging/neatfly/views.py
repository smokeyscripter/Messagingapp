# from django.shortcuts import render

# def home(request):
#     return render(request, 'neatfly/index.html')
    
# def about(request):
#     return render(request, 'neatfly/about.html')

# def login_view(request):
#     return render(request, 'neatfly/login_view.html')

# def temp(request):
#     return render(request, 'neatfly/temp.html')

# def signup(request):
#     return render(request, 'neatfly/signup_view.html')

from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return render(request, "neatfly/index.html")


def login(request):
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
            return render(request, "neatfly/login_view.html", {
                "message": "Invalid username and/or password."
            })
def signup(request):
    if request.method == "POST":
        # pfp = request.FILES["picture"]
        # fs = FileSystemStorage()
        # name = fs.save(pfp.name, pfp)
        # url = fs.url(name)
        # print(url)
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        print(username)
        # email = request.POST["email"]
        # try:
        #     user = User.objects.create_user(username=username, email=email, password=password, picture=url)
        # except:
        #     return JsonResponse({
        #         "message": "error occurred while saving your profile"
        #     })
        # return HttpResponse(user.picture)
    elif request.method == "GET":
        return render(request, "neatfly/signup_view.html")