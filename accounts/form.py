from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Doctor,Patient

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    profilepicture = forms.ImageField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.phone_number=self.cleaned_data.get('phone_number')
        doctor.address=self.cleaned_data.get('address')
        doctor.city=self.cleaned_data.get('city')
        doctor.state=self.cleaned_data.get('state')
        doctor.pincode=self.cleaned_data.get('pincode')
        doctor.profilepicture=self.cleaned_data.get('profile_picture')
        doctor.save()
        return user

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    profilepicture = forms.ImageField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.phone_number=self.cleaned_data.get('phone_number')
        patient.address=self.cleaned_data.get('address')
        patient.city=self.cleaned_data.get('city')
        patient.state=self.cleaned_data.get('state')
        patient.pincode=self.cleaned_data.get('pincode')
        patient.profilepicture=self.cleaned_data.get('profile_picture')
        patient.save()
        return user
