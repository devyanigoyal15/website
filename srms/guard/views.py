from django.shortcuts import render,redirect
from web.models import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from web.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'web/logi.html')

def login(request):
    return render(request, 'web/login.html')

@login_required
def home(request):
    l=le.objects.filter(status=1)
    return render(request, 'web/guard.html',{"leave":l})
