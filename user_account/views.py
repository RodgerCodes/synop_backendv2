from rest_framework.views import APIView
from .serializers import Stationserializer, Userserializer
from rest_framework.permissions import IsAuthenticated
from .models import User, Station
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class GetStations(APIView):
    def get(self, request):
        stations = Station.objects.all()
        serializer = Stationserializer(stations,many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

