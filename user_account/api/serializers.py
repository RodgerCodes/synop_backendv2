from rest_framework import serializers
from ..models import User, Station


class Stationserializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
