from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data, synop
from django.http import Http404
from user_account.models import Station
from user_account.serializers import Stationserializer
from .serializers import DataSerializer, SynopSerializer
from datetime import datetime


# Create your views here.

# app apis
class GetStationData(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Station.objects.get(station_number=pk)
        except:
            raise Http404

    def get(self, request, station_number):
        user = request.user
        station = self.get_object(station_number)
        print(user.station)
        if user.station != station:
            return Response({'message': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        station_data = Data.objects.filter(station_id=station).prefetch_related('synop_data')
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
            return Response({'message': 'Data successfully submitted'})


class EditData(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
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

    def get_object(self, pk):
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


# web apis start here
class GetStations(APIView):
    """
    View for getting all stations
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stations = Station.objects.all()
        serializer = Stationserializer(stations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class GetSingleStation(APIView):
    """
    View for getting single station details and its data
    """
    permission_classes =[IsAuthenticated]

    def get(self, request, station_id):
        station = Station.objects.prefetch_related('station_info').get(id=station_id)
        serializer = Stationserializer(station, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class GetSingleCode(APIView):
    """
    View for getting single synop code with its data
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, synop_id):
        code = synop.objects.select_related('data').get(id=synop_id)
        serializer = SynopSerializer(code, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodayCodes(APIView):
    """
    View for getting synop codes submitted today
    """
    permission_classes =[IsAuthenticated]

    def get(self, request):
        today = datetime.today()
        codes = synop.objects.filter(created=today)
        serializer = SynopSerializer(codes, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
