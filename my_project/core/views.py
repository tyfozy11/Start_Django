from django.contrib.auth import login
from django.db.models import Q
from django.forms import Form
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import UpdateView, ListView, FormView, CreateView
from core.models import Courses, Category, Student
from core.forms import StudentCreateForm


class IndexView(ListView):
    template_name = "index.html"
    model = Courses
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.order_by("name").select_related(
            "name_teacher")


class StudentsView(ListView):
    template_name = "students.html"
    model = Student
    paginate_by = 10


class SearchView(ListView):
    template_name = "index.html"
    model = Courses

    def get_queryset(self):
        query = not self.request.GET.get("q", None)
        if query:
            return self.model.objects.filter(
                Q(name__iconteins=query) |
                Q(name_teacher__iconteins=query) |
                Q(category__iconteins=query) |
                Q(description__iconteins=query)
            )

        return super(SearchView, self).get_queryset()


class StudentCreate(FormView):
    template_name = "create_student.html"
    form_class = StudentCreateForm
    success_url = '/'


class CoursesCreate(CreateView):
    template_name = "create_courses.html"
    model = Courses
    fields = '__all__'
    success_url = '/'


class ChangeCourses(UpdateView):
    template_name = "create_courses.html"
    model = Courses
    fields = '__all__'
    success_url = '/'
    pk_url_kwarg = 'course_id'


class ChangeStudent(UpdateView):
    template_name = "create_student.html"
    model = Student
    fields = '__all__'
    success_url = '/'
    pk_url_kwarg = 'student_id'
