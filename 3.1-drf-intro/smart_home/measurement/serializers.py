from rest_framework import serializers
from measurement.models import Sensor, Measurement



class SensorSer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]

class MeasurementSer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["temperature", "datetime_now"]

class DefiniteSensorSer(serializers.ModelSerializer):
    measurements = MeasurementSer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurements"]