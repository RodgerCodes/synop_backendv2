from django.urls import path, include
from . import views

app_name="accounts"
urlpatterns = [
    path('', views.getHome, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('api/user/', include('user_account.api.urls')),
]