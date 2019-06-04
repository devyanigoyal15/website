from django.shortcuts import render, redirect
from web.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from web.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'web/log.html')


def login(request):
    return render(request, 'web/login.html')


@login_required(login_url='/buscont/home/')
def home(request):
    return render(request, 'web/busadmin.html')


def upd(request):
    buss.objects.filter(routeno=request.GET.get("routeno")).update(busno=request.GET.get("busno"))
    return redirect("home")
