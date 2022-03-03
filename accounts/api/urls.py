from django.urls import path
from accounts.api.views import (
    registration_view
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account_api"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
  
]
