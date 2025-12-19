from django.urls import path
from . import api_views

urlpatterns = [
    path('patients/', api_views.patient_list_api),
    path('patients/<int:pk>/', api_views.patient_detail_api),
    path('patients/add/', api_views.patient_create_api),
    path('patients/update/<int:pk>/', api_views.patient_update_api),
    path('patients/delete/<int:pk>/', api_views.patient_delete_api),
]
