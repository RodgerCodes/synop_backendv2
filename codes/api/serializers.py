from rest_framework import serializers
from ..models import Data, synop
from user_account.models import Station
from user_account.api.serializers import Stationserializer

class synopSerializer(serializers.ModelSerializer):
    class Meta:
        model = synop
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    synop_data = synopSerializer(required=False)
    class Meta:
        model = Data
        fields = '__all__'

    def create(self, validated_data):
        data = super().create(validated_data)
        stNumber = self.context.get("station_number")
        station = Station.objects.get(station_number=stNumber)
        code = self.context.get('synop')
        synopInstance = synop.objects.create(
             code = code,
             data = data,
             station = station
        )
        synopInstance.save()
        return data


class SynopSerializer(serializers.ModelSerializer):
    station = Stationserializer(required=False)
    class Meta:
        model = synop   
        fields = '__all__'
