from django.shortcuts import render,redirect
from .models import registration
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.

def home(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if registration.objects.filter(email=email).exists():
            info = registration.objects.get(email=email)
            return render(request, 'dash.html',{'user':info})
    return  render (request,'home.html')


def demo(request):
    return  render (request,'demo.html')


def resume(request):
    return  render (request,'resume.html')

def signin(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if registration.objects.filter(email=email).exists():
            info = registration.objects.get(email=email)
            return render(request, 'dash.html',{'user':info})
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if registration.objects.filter(email=email).filter(pwd=pwd).exists():
            info1 = registration.objects.get(email=email)
            request.session['std_logged'] = email
            return render(request, 'dash.html',{'user':info1})
        else:
            messages.info(request, 'Please Enter Valid Credentials !!!!')
            return redirect('home')
    else:
        return redirect('home')
    

def signup(request):
    if request.method == 'POST' and request.FILES['ppic']:
            name = request.POST['name']
            mobile = request.POST['mobile']
            profile = request.POST['profile']
            title = request.POST['title']
            ppic = request.FILES['ppic']
            email = request.POST['email']
            social = request.POST['social']
            pwd = request.POST['pwd']
            rpwd = request.POST['rpwd']
            if pwd==rpwd:
                if registration.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist !!!!')
                    return redirect('home')
                else:
                    user=registration(name=name,mobile=mobile,profile=profile,title=title,ppic=ppic,email=email,social=social,pwd=pwd)
                    user.save()
                    messages.info(request, 'Registered Successfully !!!!')
                    return redirect('home')
            else:
                messages.info(request, 'Both Passwords Are Different !!!!')
                return redirect('home')
    return  redirect ('home')


def signout(request):
    del request.session['std_logged']
    return redirect('home')


def view_resume(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        if registration.objects.filter(email=email).exists():
            info = registration.objects.get(email=email)
            return render(request, 'view_resume.html',{'user':info})
    return  redirect ('home')