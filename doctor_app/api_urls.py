from django.urls import path
from . import api_views

urlpatterns = [
    path('doctors/', api_views.doctor_list_api),
    path('doctors/<int:pk>/', api_views.doctor_detail_api),
    path('doctors/add/', api_views.doctor_create_api),
    path('doctors/update/<int:pk>/', api_views.doctor_update_api),
    path('doctors/delete/<int:pk>/', api_views.doctor_delete_api),
]
