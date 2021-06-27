from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import RememberForm
from .models import Remember
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'remember/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'remember/signupuser.html', {'form': UserCreationForm()})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(currentremember)
        except IntegrityError:
            return render(request, 'remember/signupuser.html', {'form': UserCreationForm(),
                                                                'error': "The username has already been taken. "
                                                                         "Please chose a new username."})

        else:
            return render(request, 'remember/signupuser.html', {'form': UserCreationForm(),
                                                                'error': "Password didn't match"})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'remember/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'remember/loginuser.html', {'form': AuthenticationForm(), 'error':"User name and password didn't match"})
        else:
            login(request, user)
            return redirect('currentremember')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createremember(request):
    if request.method == 'GET':
        return render(request, 'remember/createremember.html', {'form': RememberForm()})
    else:
        try:
            form = RememberForm(request.POST)
            newremember = form.save(commit=False)
            newremember.user = request.user
            newremember.save()
            return redirect('currentremember')
        except ValueError:
            return render(request, 'remember/createremember.html', {'form': RememberForm(), 'error': "Bad data passed "
                                                                                                     "in! "
                                                                                                     " Please again"})


@login_required
def currentremember(request):
    remembers = Remember.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'remember/currentremember.html', {'remembers': remembers})


@login_required
def completedremember(request):
    remembers = Remember.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'remember/completedremember.html', {'remembers': remembers})


@login_required
def viewremember(request, remember_pk):
    remember = get_object_or_404(Remember, pk=remember_pk, user=request.user)
    if request.method == 'GET':
        form = RememberForm(instance=remember)
        return render(request, 'remember/viewremember.html', {'remember': remember, 'form': form})
    else:
        try:
            form = RememberForm(request.POST, instance=remember)
            form.save()
            return redirect('currentremember')
        except ValueError:
            return render(request, 'remember/viewremember.html', {'remember': remember, 'form': form,
                                                                  'error': 'Bad Info!'})


@login_required
def completeremember(request, remember_pk):
    remember = get_object_or_404(Remember, pk=remember_pk, user=request.user)
    if request.method == 'POST':
        remember.datecompleted = timezone.now()
        remember.save()
        return redirect('currentremember')


def deleteremember(request, remember_pk):
    remember = get_object_or_404(Remember, pk=remember_pk, user=request.user)
    if request.method == 'POST':
        remember.delete()
        return redirect('currentremember')


def about(requset):
    return render(requset, 'remember/about.html')
