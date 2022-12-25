from django.urls import path
from . import views

app_name="codes"
urlpatterns = [
    path('dahboard/', views.GetDashboard, name='dashboard'),

    # web apis
    # path('all-stations/', GetStations.as_view()),
    # path('station/<station_id>/', GetSingleStation.as_view()),
    # path('today-codes/',TodayCodes.as_view()),
    # path('codes/<synop_id>/', GetSingleCode.as_view()),
]