from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data
from django.http import Http404
from user_account.models import Station
from .serializers import DataSerializer

# Create your views here.
class GetStationData(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(pk):
        try:
            return Station.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, station_number):
        user = request.user
        station = self.get_object(station_number)
        if user.station != station.id:
            return Response({'message':'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        station_data = Station.objects.filter(station = station.id)
        serializer = DataSerializer(station_data, many=True)
        return Response(serializer.data)
