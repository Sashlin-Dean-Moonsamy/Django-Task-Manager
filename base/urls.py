from django.urls import path, include
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sign-up/', views.register_page, name='register-page'),
]