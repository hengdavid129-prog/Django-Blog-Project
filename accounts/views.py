from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not firstname or not lastname or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('accounts:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return redirect('accounts:register')

        try:
            user = User.objects.create_user(
                username=email,
                email=email, 
                password=password,
                first_name=firstname,
                last_name=lastname,
            )

            UserProfile.objects.create(user=user, role='reader')


            messages.success(request, 'Account created successfully.')
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, 'An error occured during registration. Please try again.')
            return render(request, 'accounts/register.html')
 
    return render(request, 'accounts/register.html')

def login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')

        next_url = request.POST.get('next')

        if not email or not password:
            messages.error(request, 'Please provide both email and password')
            return redirect('accounts:login')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome Back, {user.first_name}')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('blog:index')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

@login_required(login_url='accounts:login')
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('accounts:login')