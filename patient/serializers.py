from rest_framework import serializers
from .models import Patient_Info

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Info
        fields = "__all__"
