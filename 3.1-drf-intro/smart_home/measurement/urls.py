from django.urls import path
from measurement import views
from .serializers import SensorSer, MeasurementSer
from .models import Sensor, Measurement



urlpatterns = [
    path("Sensor/", views.GetAllSensor.as_view()),
    path("Sensor/<pk>/", views.GetDefiniteSensor.as_view()),
    path("SensorUP/<pk>/", views.UpdateSensor.as_view()),
    path("Meas/", views.GetAllMeas.as_view()),

    path('CreateSensor/', views.CreateSensor.as_view(queryset=Sensor.objects.all(), serializer_class=SensorSer), name='user-list'),
    path('CreateMeas/', views.CreateSensor.as_view(queryset=Measurement.objects.all(), serializer_class=MeasurementSer), name='user-list')
]
