from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Sensor, Measurement
from .serializers import SensorSer, MeasurementSer, DefiniteSensorSer



class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSer
    permission_classes = [IsAdminUser]

class GetAllSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSer

class GetDefiniteSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DefiniteSensorSer

class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSer
    permission_classes = [IsAdminUser]

class GetAllMeas(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSer

class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSer
