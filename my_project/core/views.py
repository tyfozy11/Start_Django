from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView
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


class ChangeCourses(CoursesCreate):
    def get_form_kwargs(self):
        form_kwargs = super(ChangeCourses, self).get_form_kwargs()
        form_kwargs['instance'] = Courses.objects.get(id=self.request.GET['courses_id'])
        return form_kwargs


class ChangeStudent(StudentCreate):

    def get_form_kwargs(self):
        form_kwargs = super(ChangeStudent, self).get_form_kwargs()
        form_kwargs['instance'] = Student.objects.get(id=self.request.GET['student_id'])
        return form_kwargs
