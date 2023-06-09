from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('doctor_register/',views.Doctor_register.as_view(), name='doctor_register'),
     path('patient_register/',views.Patient_register.as_view(), name='patient_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]