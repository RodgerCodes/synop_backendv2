from rest_framework import serializers
from .models import Data, synop


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class SynopSerializer(serializers.ModelSerializer):
    class Meta:
        model = synop
        fields = '__all__'
