from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login, name='login'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # PASSWORD RESET URLS
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
