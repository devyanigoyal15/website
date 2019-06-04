from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=50)
    dob = models.TextField(max_length=11)
    gender = models.CharField(max_length=18)
    address = models.CharField(max_length=100)
    email=models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    desg = models.CharField(max_length=50)

class le(models.Model):
    id = models.AutoField(primary_key=True)
    rno = models.IntegerField(null=True,blank=True)
    heading = models.CharField(max_length=50,null=True)
    sender = models.CharField(max_length=50,null=True)
    status = models.IntegerField(null=True,blank=True)
    reason = models.CharField(max_length=100,null=True)
    df = models.TextField(max_length=11,null=True)
    dt = models.TextField(max_length=11,null=True)
    name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class buss(models.Model):
    busno= models.CharField(max_length=50)
    routeno=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.routeno+self.busno

class s(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=100)
    pno = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()
    left=models.IntegerField()
    type=models.CharField(max_length=100)
    status = models.IntegerField(null=True, blank=True)

class d(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=100)
    pno = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()
    left=models.IntegerField()
    type=models.CharField(max_length=100)
    status = models.IntegerField(null=True, blank=True)

class t(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    add = models.CharField(max_length=100)
    pno = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()
    left=models.IntegerField()
    type=models.CharField(max_length=100)
    status = models.IntegerField(null=True, blank=True)