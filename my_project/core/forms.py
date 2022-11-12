from django import forms
from django.contrib.auth.models import User

from core.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



