from django.urls import path
from . import views

urlpatterns = [
     path('station/<int:station_number>/', views.GetStationData.as_view()),
    path('submit-data/', views.SubmitData.as_view()),
    path('edit-data/', views.EditData.as_view()),
    path('del-data', views.DeleteCode.as_view()),
]
