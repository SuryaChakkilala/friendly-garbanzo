from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User
from .models import *
from accounts.forms import CustomUserCreationForm as RegisterUserForm
from accounts.forms import CustomUserChangeForm as UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account with username {request.user.username} has succesfully been updated!')
            return redirect('profile')
    form = UserUpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'pages/profile.html', context)

def home(request):
    if request.user.is_authenticated:
        bg_img = PageImage.objects.get(name='homebg')
    else:
        bg_img = PageImage.objects.get(name='homebg-unauthenticated')
    link1 = Event.objects.get(name='conference').link
    link2 = Event.objects.get(name='paper-presentation').link
    context = {'link1': link1, 'link2': link2, 'bg_img': bg_img}
    return render(request, 'pages/home.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def conferences(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to view the conference.')
        return redirect('login')
    obj = Event.objects.get(name='conference')
    context = {'link': obj.link}
    return render(request, 'pages/conferences.html', context)

def paper_presentations(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to view the paper presentation.')
        return redirect('login')
    obj = Event.objects.get(name='paper-presentation')
    context = {'link': obj.link}
    return render(request, 'pages/paper_presentations.html', context)

def events(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to view the events page.')
        return redirect('login')
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'pages/events.html', context)

def register(request, event_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to register for events.')
        return redirect('login')
    event = Event.objects.get(id=event_id)
    event.registered_users.add(request.user)
    event.save()
    return redirect('events')

def unregister(request, event_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to unregister for events.')
        return redirect('login')
    event = Event.objects.get(id=event_id)
    event.registered_users.remove(request.user)
    event.save()
    return redirect('events')

def virtual_tour(request):
    return render(request, 'pages/virtual_tour.html')