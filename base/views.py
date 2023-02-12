from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import views as auth_views, authenticate, login, logout

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'base/home.html')


def register(request):
    if request.method == 'POST':
        # Process the form data
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            # Create a new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            # Login the user and redirect to the dashboard
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an error message
            return render(request, 'base/register.html', {
                'error_message': 'Passwords do not match'
            })
    else:
        return render(request, 'base/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'base/dashboard.html')
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'POST':
        # Process the login form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user and redirect to the dashboard
            login(request, user)
            return redirect('dashboard')
        else:
            # Return an error message
            return render(request, 'base/home.html', {
                'error_message': 'Invalid login credentials'
            })
    else:
        return render(request, 'base/home.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def password_reset(request):
    if request.method == 'POST':
        # Process the form submission
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            # Send the password reset email
            auth_views.PasswordResetView.as_view()(
                request, email_template_name='base/password_reset_confirm.html')
            # Redirect to the password reset done page
            return redirect('password_reset_done')
        except User.DoesNotExist:
            # Return an error message
            return render(request, 'base/password_reset_form.html', {
                'error_message': 'Email address not found'
            })
    else:
        return render(request, 'base/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'base/password_reset_done.html')

# def password_reset_confirm(request, uidb64, token):
#     return render(request, 'base/password_reset_confirm.html')

# def password_reset_complete(request):
#     return render (request, 'base/password_reset_complete.html')
