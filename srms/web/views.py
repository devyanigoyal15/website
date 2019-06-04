from django.shortcuts import render,redirect
from web.models import *
from django.db.models import Q,F
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def signup(request):
    return render(request, 'web/signup.html')

def login(request):
    return render(request, 'web/login.html')

def bus(request):
    b1=buss.objects.filter(routeno=1)
    b2 = buss.objects.filter(routeno=2)
    b3 = buss.objects.filter(routeno=3)
    return render(request, 'web/bus.html',{"bb":b1,"bbb":b2,"a":b3})

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'web/login.html', {'u':username})
    else:
        form = UserRegistrationForm()
    return render(request,'web/register.html',{'form':form})

@login_required(login_url='/web/home/')
def home(request):
    return render(request, 'web/index1.html')

@login_required
def ll(request):
    l = le.objects.filter(sender=request.user.email)
    return render(request, 'web/leave.html',{"leave":l})

def send(request):
    l = le()
    user=request.user
    l.sender = user.email
    l.status = 0
    l.heading = request.GET.get("heading")
    l.name = request.GET.get("name")
    l.rno = request.GET.get("rno")
    l.reason = request.GET.get("reason")
    l.df = request.GET.get("df")
    l.dt = request.GET.get("dt")
    l.save()
    return redirect("ll")

def disp(request):
    s=staff.objects.all()
    l=le.objects.all()
    return render(request,"web/disp.html",{"staff":s,"leave":l})

def rotate(request):
    return render(request, 'web/360.html')

@login_required
def room(request):
    s.objects.filter(email=request.user.email).update(left=F('total') - F('id'))
    d.objects.filter(email=request.user.email).update(left=F('total') - F('id'))
    t.objects.filter(email=request.user.email).update(left=F('total') - F('id'))
    ss = s.objects.order_by('id').reverse().first()
    dd = d.objects.order_by('id').reverse().first()
    tt = t.objects.order_by('id').reverse().first()
    return render(request, 'web/room.html',{"ss":ss,"dd":dd,"tt":tt})

@login_required
def sbook(request):
    return render(request, 'web/book.html')

@login_required
def dbook(request):
    return render(request, 'web/book1.html')

@login_required
def tbook(request):
    return render(request, 'web/book2.html')

def singler(request):
    s1 = s()
    user=request.user
    s1.email = user.email
    s1.name = request.GET.get("name")
    s1.pno = request.GET.get("pno")
    s1.add=request.GET.get("address")
    s1.date = datetime.datetime.now()
    s1.total=40
    s1.left=0
    s1.type='s'
    s1.status=0
    s1.save()
    return redirect("room")

def double(request):
    s1 = d()
    user=request.user
    s1.email = user.email
    s1.name = request.GET.get("name")
    s1.pno = request.GET.get("pno")
    s1.add=request.GET.get("address")
    s1.date = datetime.datetime.now()
    s1.total=80
    s1.left=0
    s1.type='d'
    s1.status=0
    s1.save()
    return redirect("room")

def triple(request):
    s1 = t()
    user=request.user
    s1.email = user.email
    s1.name = request.GET.get("name")
    s1.pno = request.GET.get("pno")
    s1.add=request.GET.get("address")
    s1.date = datetime.datetime.now()
    s1.total=120
    s1.left=0
    s1.type='t'
    s1.status=0
    s1.save()
    return redirect("room")



