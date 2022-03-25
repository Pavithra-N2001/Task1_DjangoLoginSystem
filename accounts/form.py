from email.mime import image
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import Doctor, User,Patient

class DoctorSignupForm(UserCreationForm):
    f_name=forms.CharField()
    l_name=forms.CharField()
    # image=forms.ImageField()
    email=forms.CharField()
    address=forms.CharField()

    class Meta(UserCreationForm.Meta):
        model =User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_doctor=True
        user.f_name=self.cleaned_data.get('f_name')
        user.l_name=self.cleaned_data.get('l_name')
        user.save()
        doctor=Doctor.objects.create(user=user)
        doctor.image=self.cleaned_data.get('image')
        doctor.email=self.cleaned_data.get('email')
        doctor.address=self.cleaned_data.get('address')
        doctor.save()
        return user
   
class PatientSignupForm(UserCreationForm):
    f_name=forms.CharField()
    l_name=forms.CharField()
    # image=forms.ImageField()
    email=forms.CharField()
    address=forms.CharField()

    class Meta(UserCreationForm.Meta):
        model =User
    
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_patient=True
        user.f_name=self.cleaned_data.get('f_name')
        user.l_name=self.cleaned_data.get('l_name')
        user.save()
        patient=Patient.objects.create(user=user)
        patient.image=self.cleaned_data.get('image')
        patient.email=self.cleaned_data.get('email')
        patient.address=self.cleaned_data.get('address')
        patient.save()
        return user

        
    


