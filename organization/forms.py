from django import forms
from .models import Project, Employee, Client, Service, Review

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'category', 'client', 'employees', 'photo', 'start_date', 'budget', 'is_completed']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'photo', 'email', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact_person', 'email', 'phone', 'logo', 'is_active']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['client', 'project', 'text', 'rating']