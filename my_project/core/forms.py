from django import forms
from core.models import Category, Courses, Group, Teacher


class StudentCreateForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    course = forms.ModelChoiceField(queryset=Courses.objects.all())


class CoursesCreateForm(forms.Form):
    name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    description = forms.CharField(widget=forms.widgets.Textarea)
    name_teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    short_list_of_course_theses = forms.CharField(widget=forms.widgets.Textarea)
