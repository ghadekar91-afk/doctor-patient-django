from rest_framework import viewsets
from .models import Doctor_Info
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor_Info.objects.all()
    serializer_class = DoctorSerializer
