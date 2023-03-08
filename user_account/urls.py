from django.urls import path, include
from . import views

app_name="accounts"
urlpatterns = [
    path('', views.getHome, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('api/user/', include('user_account.api.urls')),

    # path
    path('stations/new/', views.CreateStation.as_view(), name="new_station"),
    path('observers/list/', views.GetObservers, name="get_observers"),
    path('observer/new/', views.NewObservers, name="new_observer"),
    path('observer/<userId>/delete/', views.RemoveObserver, name="Remove_observer"),
    path('reassign-observer/<userID>/', views.ReassignObserver, name="reasssign_observer"),
    path('single-station/<stationId>/', views.GetSingleStation, name="single_station")
]