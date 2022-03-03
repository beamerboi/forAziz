from django.contrib import admin
from django.urls import path, include
from accounts import views

app_name="account"

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register_view)
]
