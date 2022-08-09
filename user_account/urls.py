from django.urls import path
from .views import GetStations

urlpatterns = [
    path('stations/', GetStations.as_view())
]