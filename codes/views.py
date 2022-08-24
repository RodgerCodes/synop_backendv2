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
            return Station.objects.get(station_number=pk)
        except:
            raise Http404

    def get(self, request, station_number):
        user = request.user
        station = self.get_object(station_number)
        if user.station != station.id:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        station_data = Station.objects.filter(station=station.id)
        serializer = DataSerializer(station_data, many=True)
        return Response(serializer.data)


class SubmitData(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        station = Station.objects.filter(station_number=request.data['station_number']).first()
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(station_id=station)
            return Response(serializer.data)


class EditData(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(pk):
        try:
            return Station.objects.get(station_number=pk)
        except:
            raise Http404

    def put(self, request):
        user = request.user
        station = self.get_object(request.data['station_number'])
        code = Data.objects.get(id=request.data['data_id'])
        if code.station_id != station.id and user.station != station.id:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        serializer = DataSerializer(code, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteCode(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(pk):
        try:
            return Data.objects.get(id=pk)
        except:
            raise Http404

    def delete(self, request):
        user = request.user
        code = self.get_object(request.data['data_id'])
        station = Station.objects.filter(id=user.station).first()
        if station.id != code.sation_id:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        code.delete()
        return Response({'message': 'Data deleted'})
