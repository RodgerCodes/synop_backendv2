from django.urls import path
from .views import GetStations, RegisterUser,MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('stations/', GetStations.as_view()),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('test/', ResetPassword.as_view())
]