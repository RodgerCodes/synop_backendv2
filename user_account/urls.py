from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.getHome, name="login"),
    path('api/user/', include('user_account.api.urls')),
]