from django.contrib.auth.models import User
from django.shortcuts import render
from application.forms import UserForm, UserInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'application/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def registration(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = info_form.save(commit=False)
            info.user = user

            info.save()
            
            registered = True
        else:
            print(user_form.errors, info_form.errors)
    else:
        user_form = UserForm()
        info_form = UserInfoForm()
    return render(request,'application/register.html',{
                                                'user_form':user_form,
                                                'info_form':info_form,
                                                'registered':registered
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('Someone tried to login and failed')
            print('Username:{} and password'.format(username,password))
            return HttpResponse('Invalid login details supplied!')

    return render(request, 'application/login.html',{})