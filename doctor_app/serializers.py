from rest_framework import serializers
from .models import Doctor_Info

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Info
        fields = "__all__"
