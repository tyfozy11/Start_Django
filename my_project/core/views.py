from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from core.models import Group, Teacher, Student


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        group = Group.objects.all()
        print(group)
        teacher = Teacher.objects.all()
        print(teacher)
        student = Student.objects.all()
        print(student)
        student_in_group = Student.objects.filter(group__name__exact="#2")
        print(student_in_group)
        first_teacher_group_id = Teacher.objects.first().group_id
        teacher_students = Student.objects.filter(group=first_teacher_group_id)
        print(teacher_students)
        student_age = Student.objects.filter(age__gt=20)
        print(student_age)
        student_email = Student.objects.filter(email__contains="gmail.com")
        print(student_email)
        teacher_students_age = Student.objects.filter(group=first_teacher_group_id, age__gt=20)
        print(teacher_students_age)
        return context


class ProfileView(DetailView):
    template_name = "profile.html"
    model = User
