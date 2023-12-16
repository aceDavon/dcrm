from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .signup_form import Sign_Up_Form


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out...')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = Sign_Up_Form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
    else:
        form = Sign_Up_Form()

    return render(request, 'register.html', {'form': form})
