"""
URL mappings for the Auth API.
"""
from django.urls import path

from authentication import views


app_name = 'authentication'

urlpatterns = [
    path('login/', views.CreateTokenView.as_view(), name='login'),
    path('resetpassword/',
         views.ResetPasswordView.as_view(),
         name='resetpassword'),
]
