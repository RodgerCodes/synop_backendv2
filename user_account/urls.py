from django.urls import path, include
from .views import GetStations, RegisterUser,MyTokenObtainPairView


urlpatterns = [
    path('api/user/', include('user_account.api.urls')),
]