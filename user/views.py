from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are succesfully logged in')
            return redirect('user:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('user:login')

    return render(request, 'login.html')



def registration_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is not available')
                return redirect('user:registration')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is not available')
                    return redirect('user:registration')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                    password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are logged in')
                    return redirect('user:dashboard')
                    user.save()
                    messages.success(request, 'You are succesfully registered')
                    return redirect('user:login')

        else:
            messages.error(request, 'Passwords is not invalid')
            return redirect('user:registration')

    else:
        return render(request, 'registration.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are succesfully logged out')
        return redirect('pages:home')
    return redirect('pages:home')
