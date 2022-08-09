from django.urls import path
from .views import GetStationData, SubmitData, EditData

urlpatterns = [
    path('station/<int:station_number>/', GetStationData.as_view()),
    path('submit-data/', SubmitData.as_view()),
    path('edit-data/', EditData.as_view())
]