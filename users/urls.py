from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import register, profile_view, edit_profile, change_password
"""Urls for users"""


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/change-password/', change_password, name='change_password'),
    path('reset-password', 
        PasswordResetView.as_view(template_name='users/reset_password.html', email_template_name='users/reset_password_email.html', success_url='reset-password/done/'),
        name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html', success_url='reset-password/complete/'), 
        name='password_reset_confirm'),
    path('reset-password/complete/',
     PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'),
      name='password_reset_complete'),
]