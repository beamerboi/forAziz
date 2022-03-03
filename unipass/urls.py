from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/api/', include('accounts.api.urls', 'account_api'),),
]
