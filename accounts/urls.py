from django.urls import path
from accounts import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', v.register, name="account-register"),
    path('scheduler/', v.scheduler, name="account-interview-schedule"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="account-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="account-logout"), 
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_done"),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),
]
