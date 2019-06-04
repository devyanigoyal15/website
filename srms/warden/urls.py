from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='web/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web/logout.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('home/acc/', views.acc, name='acc'),
    path('home/rej/', views.rej, name='rej'),
]