from rest_framework.views import APIView
from .serializers import Stationserializer, Userserializer
from rest_framework.permissions import IsAuthenticated
from .models import User, Station
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class GetStations(APIView):
    def get(self, request):
        stations = Station.objects.all()
        serializer = Stationserializer(stations,many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    def post(self, request):
        station_number = int(request.data['station_num'])
        station = Station.objects.filter(station_number=station_number).first()
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(station=station)
        return Response({'message':'Account created successfully'}, status=status.HTTP_201_CREATED)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

