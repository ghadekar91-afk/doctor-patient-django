from django.urls import path
from . import views, auth_views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('doctor/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctor/create/', views.doctor_create, name='doctor_create'),
    path('doctor/update/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctor/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),

    # Authentication
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('signup/', auth_views.signup_view, name='signup'),
]
