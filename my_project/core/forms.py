from django import forms
from core.models import Category, Courses, Group, Teacher, Student


class StudentCreateForm(forms.Form):
    name = forms.CharField(label='Ім\'я')
    age = forms.IntegerField(label='Вік', min_value=18)
    email = forms.EmailField(label='Еmail')
    group = forms.ModelChoiceField(empty_label='Оберіть групу', label='Група', queryset=Group.objects.all())
    course = forms.ModelChoiceField(empty_label='Оберіть курс', label='Назва курсу', queryset=Courses.objects.all())

    def create_student(self):
        student = Student.objects.create(
            name=self.cleaned_data['name'],
            age=self.cleaned_data['age'],
            email=self.cleaned_data['email'],
            group=self.cleaned_data['group'],
            course=self.cleaned_data['course']
        )
        return student

    def clean_name(self):
        name = self.cleaned_data['name']
        if ' ' in name:
            raise forms.ValidationError('Не має містити пробілів!')
        return name


class CoursesCreateForm(forms.Form):
    name = forms.CharField(label='Назва курсу')
    category = forms.ModelChoiceField(empty_label='Оберіть категорію', label='Категорія',
                                      queryset=Category.objects.all())
    description = forms.CharField(widget=forms.widgets.Textarea, label='Короткий опис')
    name_teacher = forms.ModelChoiceField(empty_label='Оберіть викладача', label='Викладач',
                                          queryset=Teacher.objects.all())
    short_list_of_course_theses = forms.CharField(widget=forms.widgets.Textarea, label='Основні тезиси')

    def create_courses(self):
        courses = Courses.objects.create(
            name=self.cleaned_data['name'],
            category=self.cleaned_data['category'],
            description=self.cleaned_data['description'],
            name_teacher=self.cleaned_data['name_teacher'],
            short_list_of_course_theses=self.cleaned_data['short_list_of_course_theses']
        )
        return courses
