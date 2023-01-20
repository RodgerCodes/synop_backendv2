from rest_framework.views import APIView
from .serializers import Stationserializer, Userserializer
from rest_framework.permissions import IsAuthenticated
from user_account.models import User, Station
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from django.conf import settings
# from django.core.mail import send_mail
from rest_framework_simplejwt.state import token_backend
# Create your views here.

class GetStations(APIView):
    def get(self, request):
        stations = Station.objects.prefetch_related('station').all()
        serializer = Stationserializer(stations,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    def post(self, request):
        station_number = int(request.data['station_num'])
        station = Station.objects.filter(station_number=station_number).first()
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(station=station)
        return Response({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token
    
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        payload = token_backend.decode(data['access'], verify=True)
        user = User.objects.get(id=payload['user_id'])
        data.update({'user': payload, 'station_number': user.station.station_number})
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


