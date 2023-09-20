from django.db import models

# Create your models here.
class signup(models.Model):
    Userid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=8)
    Address = models.CharField(max_length=100)
    PhoneNo = models.IntegerField()
    Date = models.DateField(auto_now=True)
    Profile_Pic = models.ImageField(upload_to='img/', null=True, blank=True)

class gallery(models.Model):
    ImgId = models.AutoField(primary_key=True)
    ImgName = models.CharField(max_length=20)
    Images = models.ImageField(upload_to='img/', null=True, blank=True)

