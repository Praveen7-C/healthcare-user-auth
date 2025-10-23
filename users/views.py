from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import SignupForm, LoginForm, EditProfileForm
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.title()}: {error}")
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'doctor':
            return redirect('doctor_dashboard')
        return redirect('patient_dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name()}!')
                if user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                return redirect('patient_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def dashboard(request):
    """Legacy dashboard view - redirects to appropriate dashboard based on user type"""
    if request.user.user_type == 'doctor':
        return redirect('doctor_dashboard')
    return redirect('patient_dashboard')

@login_required
def patient_dashboard(request):
    """Patient-specific dashboard"""
    context = {
        'user': request.user,
        'recent_activities': get_recent_activities(request.user),
        'address': f"{request.user.address_line1}, {request.user.city}, {request.user.state} - {request.user.pincode}"
    }
    return render(request, 'users/patient_dashboard.html', context)

@login_required
def doctor_dashboard(request):
    """Doctor-specific dashboard"""
    if request.user.user_type != 'doctor':
        return redirect('patient_dashboard')
        
    context = {
        'user': request.user,
        'recent_activities': get_recent_activities(request.user),
        'address': f"{request.user.address_line1}, {request.user.city}, {request.user.state} - {request.user.pincode}"
    }
    return render(request, 'users/doctor_dashboard.html', context)

def get_recent_activities(user):
    # This is a placeholder. In a real app, you would fetch actual activities
    # from your database based on the user type
    if user.user_type == 'doctor':
        return [
            {'type': 'appointment', 'title': 'New appointment scheduled', 'time': '2 hours ago', 'icon': 'calendar'},
            {'type': 'patient', 'title': 'New patient registered', 'time': '5 hours ago', 'icon': 'user-plus'},
            {'type': 'prescription', 'title': 'Prescription reviewed', 'time': '1 day ago', 'icon': 'file-medical'},
        ]
    else:
        return [
            {'type': 'appointment', 'title': 'Upcoming appointment tomorrow', 'time': 'In 1 day', 'icon': 'calendar'},
            {'type': 'prescription', 'title': 'New prescription added', 'time': '2 days ago', 'icon': 'pills'},
            {'type': 'test', 'title': 'Lab test results ready', 'time': '3 days ago', 'icon': 'flask'},
        ]

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'form': form})
