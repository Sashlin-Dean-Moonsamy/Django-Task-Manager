from django.urls import path, include
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.register_page, name='register-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]