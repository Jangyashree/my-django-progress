from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random

def registration(request):
    EUMFO=UserMF()
    EPMFO=ProfileMF()
    d={'EUMFO':EUMFO,'EPMFO':EPMFO}


    if request.method=='POST' and request.FILES:
        NMUMFDO=UserMF(request.POST)
        NMPMFDO=ProfileMF(request.POST,request.FILES)
        if NMUMFDO.is_valid() and NMPMFDO.is_valid():
            MUMFDO=NMUMFDO.save(commit=False)
            pw=NMUMFDO.cleaned_data['password']
            MUMFDO.set_password(pw)
            MUMFDO.save()

            #Done with user
            #start Profile

            MPMFDO=NMPMFDO.save(commit=False)
            MPMFDO.username=MUMFDO
            MPMFDO.save()


            send_mail('Registration',
                      'Registration is Successfull.',
                      'kjpatra739@gmail.com',
                      [MPMFDO.email],
                      fail_silently=False)
            
            return HttpResponse('Registration is Successfully..')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'registration.html',d)



def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'Home.html',d)
    
    return render(request,'Home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponseRedirect('User is not Active or Not present in Database')

    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('Home'))


@login_required
def display_details(request):
    LUN=request.session.get('username')
    UO=User.objects.get(username=LUN)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO, 'PO':PO}
    return render(request,'display_details.html',d)


@login_required
def change_password(request):
    if request.method=='POST':
        LUN=request.session.get('username')
        UO=User.objects.get(username=LUN)
        np=request.POST['np']
        UO.set_password(np)
        UO.save()
        return HttpResponse('Password is Changed')
    
    return render(request,'change_password.html')



def forgot_password(request):
    if request.method=='POST':
        username=request.POST['username']

        UO=User.objects.filter(username=username)

        if UO:
            request.session['fp']=username
            return HttpResponseRedirect(reverse('reset_password'))
        else:
            return HttpResponse('Invalid Username')
    return render(request,'forgot_password.html')
    


def reset_password(request):
    if request.method=='POST':
        np=request.POST.get('new_password')
        username=request.session.get('fp')

        user=User.objects.get(username=username)
        user.set_password(np)
        user.save
        return HttpResponse('Password reset successful')

    return render(request, 'reset_password.html')


















def verify_otp(request):
    email = request.session.get('reset_email')
    if not email:
        return HttpResponse("Session expired. Try again.")
    if request.method == 'POST':
        entered_otp = request.POST['otp']
        PO = Profile.objects.get(email=email)
        if PO.otp == entered_otp:
            return HttpResponseRedirect(reverse('reset_password'))
        else:
            return HttpResponse("Invalid OTP")
    return render(request, 'verify_otp.html')

