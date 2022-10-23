from django import forms
from core.models import Category, Courses, Group, Teacher, Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
