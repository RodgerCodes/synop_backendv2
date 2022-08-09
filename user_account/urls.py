from django.urls import path
from .views import GetStations, RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('stations/', GetStations.as_view())
]