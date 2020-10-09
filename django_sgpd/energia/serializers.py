from rest_framework import serializers
from .models import Meter, Ueb, Reading


class MeterSerializer(serializers.ModelSerializer):
    # reds = serializers.ReadOnlyField(source='readings')
    
    class Meta:
        model = Meter
        fields = '__all__'
        


class UebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ueb
        fields = '__all__'


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'
