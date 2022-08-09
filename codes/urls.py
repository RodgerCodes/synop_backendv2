from django.urls import path
from .views import GetStationData

urlpatterns = [
    path('station/<int:station_number>/', GetStationData.as_view())
]