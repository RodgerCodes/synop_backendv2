from django.urls import path
from .views import GetStationData, SubmitData, EditData, DeleteCode,GetStations, GetSingleCode, GetSingleStation,TodayCodes

urlpatterns = [
    path('station/<int:station_number>/', GetStationData.as_view()),
    path('submit-data/', SubmitData.as_view()),
    path('edit-data/', EditData.as_view()),
    path('del-data', DeleteCode.as_view()),

    # web apis
    path('all-stations/', GetStations.as_view()),
    path('station/<station_id>/', GetSingleStation.as_view()),
    path('today-codes/',TodayCodes.as_view()),
    path('codes/<synop_id>/', GetSingleCode.as_view()),
]