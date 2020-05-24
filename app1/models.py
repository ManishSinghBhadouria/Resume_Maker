from django.db import models
from django.utils import timezone
# Create your models here.

class registration(models.Model):
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=100)
    ppic = models.FileField(upload_to='media', null=True, blank=True)
    title=models.CharField(max_length=100)
    profile=models.TextField()
    mobile=models.CharField(max_length=100)
    social=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email


class skill(models.Model):
    email=models.EmailField(max_length=100)
    skil=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email

class education(models.Model):
    email=models.EmailField(max_length=100)
    college=models.CharField(max_length=50)
    std=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email


class project(models.Model):
    email=models.EmailField(max_length=100)
    pname=models.CharField(max_length=50)
    pduration=models.CharField(max_length=100)
    pdesc=models.TextField()
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email



class language(models.Model):
    email=models.EmailField(max_length=100)
    speak=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email

