# accounts/urls.py
from django.urls import path
from .views import (
    register, LoginView, ProtectedView, ProfileView,
    request_password_reset, verify_otp, reset_password_final,verify_email
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<uidb64>/<token>/', verify_email, name='verify-email'),
     path('request-password-reset/', request_password_reset, name='request-password-reset'),
    path('verify-otp/', verify_otp, name='verify-otp'),
    path('reset-password-final/', reset_password_final, name='reset-password-final'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),  # Now this is under /accounts/
    path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(), name='api_login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('request-password-reset/', views.request_password_reset, name='request_password_reset'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password-final/', views.reset_password_final, name='reset_password_final'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]
