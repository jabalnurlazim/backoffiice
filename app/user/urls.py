"""
URL mappings for the User API.
"""
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('', views.ManageUserView.as_view(), name='me'),
    path('all/', views.GetUsersView.as_view({'get': 'list'}), name='all'),
]
