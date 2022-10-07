from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from core.models import Group, Teacher, Student


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        group = Group.object.all()
        print(group)
        teacher = Teacher.object.all()
        print(teacher)
        student = Student.object.all()
        print(student)
        student_in_group = Student.object.filter(group="#2")
        print(student_in_group)
        teacher_students = Student.object.filter()
        print(group)
        student_age = Student.object.filter(age__gt=20)
        print(student_age)
        student_email = Student.object.filter(email="gmail.com")
        print(student_email)
        return context


class ProfileView(DetailView):
    template_name = "profile.html"
    model = User
