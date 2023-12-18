from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .signup_form import Sign_Up_Form
from .models import Customer
from .icons_generator import icons_generator


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


def show_customer(request, pk):
    if request.user.is_authenticated:
        icons = icons_generator(height=20, width=20)
        skype = icons.skype_icon()
        twitter = icons.twitter_icon()
        facebook = icons.facebook_icon()
        linkedin = icons.linkedin_icon()
        instagram = icons.instagram_icon()

        try:
            customer = Customer.objects.get(pk=pk)
            return render(request, 'show_customer.html', {'customer': customer, 'facebook_icon': facebook, 'instagram_icon': instagram, 'twitter_icon': twitter, 'skype_icon': skype, 'linkedin_icon': linkedin})
        except Customer.DoesNotExist:
            messages.error(request, 'Customer not found')
            return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view that page!')
        return redirect('home')
