from rest_framework import serializers
from .models import User, Station


class Stationserializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
