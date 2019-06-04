from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='web/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web/logout.html'), name='logout'),
    path('bus/', views.bus, name='bus'),
    path('home/', views.home, name='home'),
    path('ll/', views.ll, name='ll'),
    path('ll/send', views.send, name='send'),
    path('register/', views.register, name='register'),
    path('rotate/', views.rotate, name='rotate'),
    path('disp/', views.disp, name='disp'),
    path('room/', views.room, name='room'),
    path('room/sbook/', views.sbook, name='sbook'),
    path('room/dbook/', views.dbook, name='dbook'),
    path('room/tbook/', views.tbook, name='tbook'),
    path('room/sbook/singler', views.singler, name='singler'),
    path('room/dbook/double', views.double, name='double'),
    path('room/tbook/triple', views.triple, name='triple'),
]