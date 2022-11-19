from django import forms
from core.tasks import alert_of_new_course
from core.models import Student, Courses


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CoursesCreateForm (forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

    def send_meal(self):
        alert_of_new_course.delay(self.cleaned_data['name'])





