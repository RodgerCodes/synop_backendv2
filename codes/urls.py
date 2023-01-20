from django.urls import path
from . import views

app_name="codes"
urlpatterns = [
    path('', views.GetDashboard, name='dashboard'),
    path('met-stations/', views.GetStations, name="get_stations"),

    # web apis
    # path('all-stations/', GetStations.as_view()),
    # path('station/<station_id>/', GetSingleStation.as_view()),
    # path('today-codes/',TodayCodes.as_view()),
    # path('codes/<synop_id>/', GetSingleCode.as_view()),
]