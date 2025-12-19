from rest_framework import viewsets
from .models import Patient_Info
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient_Info.objects.all()
    serializer_class = PatientSerializer
