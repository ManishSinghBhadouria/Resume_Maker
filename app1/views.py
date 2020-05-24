from django.shortcuts import render,redirect
from .models import registration,education,skill,project,language
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
            edu = education.objects.filter(email=email)
            lan = language.objects.filter(email=email)
            pro = project.objects.filter(email=email)
            ski = skill.objects.filter(email=email)
            return render(request, 'dash.html',{'user':info,'lan':lan,'pro':pro,'ski':ski,'edu':edu})
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if registration.objects.filter(email=email).filter(pwd=pwd).exists():
            info = registration.objects.get(email=email)
            request.session['std_logged'] = email
            edu = education.objects.filter(email=email)
            lan = language.objects.filter(email=email)
            pro = project.objects.filter(email=email)
            ski = skill.objects.filter(email=email)
            return render(request, 'dash.html',{'user':info,'lan':lan,'pro':pro,'ski':ski,'edu':edu})
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
            request.session['std_logged'] = email
            edu = education.objects.filter(email=email)
            lan = language.objects.filter(email=email)
            pro = project.objects.filter(email=email)
            ski = skill.objects.filter(email=email)
            return render(request, 'view_resume.html',{'user':info,'lan':lan,'pro':pro,'ski':ski,'edu':edu})
    return  redirect ('home')


def addedu(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        std = request.POST['std']
        year = request.POST['year']
        college = request.POST['college']
        user = education(email=email,year=year,std=std,college=college)
        user.save()
        messages.info(request, 'Added Successfully !!!!')
        return redirect('signin')
    return  redirect ('home')


def addpro(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        pduration = request.POST['pduration']
        pdesc = request.POST['pdesc']
        pname = request.POST['pname']
        user = project(email=email,pduration=pduration,pdesc=pdesc,pname=pname)
        user.save()
        messages.info(request, 'Added Successfully !!!!')
        return redirect('signin')
    return  redirect ('home')


def addski(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        skil = request.POST['skil']
        user = skill(email=email,skil=skil)
        user.save()
        messages.info(request, 'Added Successfully !!!!')
        return redirect('signin')
    return  redirect ('home')


def addlan(request):
    if request.session.has_key('std_logged'):
        email = request.session.get('std_logged')
        speak = request.POST['speak']
        user = language(email=email,speak=speak)
        user.save()
        messages.info(request, 'Added Successfully !!!!')
        return redirect('signin')
    return  redirect ('home')



# {% for pr in pro %}   

# {% endfor %}