from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Import ViewSets
from doctor_app.api_views import DoctorViewSet
from patient.api_views import PatientViewSet   # <-- FIXED (must match your folder name)

# DRF Router
router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML Views
    path('', include('doctor_app.urls')),
    path('', include('patient.urls')),      # <-- FIXED (lowercase folder name)

    # REST API
    path('api/', include(router.urls)),
]
