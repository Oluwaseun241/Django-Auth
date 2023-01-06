from django.shortcuts import render, redirect
from .forms import RegisterForm
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
            return render(request, 'login.html', {
                'error_message': 'Invalid login credentials'
            })
    else:
        return render(request, 'base/home.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

# def register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'An error occurred during registration')

#     return render(request, 'base/register_login.html', {'form': form})

def password_reset(request):
    return render(request, 'base/password_reset.html')