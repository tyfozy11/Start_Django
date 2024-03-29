from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import UpdateView, ListView, FormView, TemplateView
from core.models import Courses, Student
from core.forms import StudentCreateForm, CoursesCreateForm

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60 * 3, key_prefix='index'), 'get')
class IndexView(ListView):
    template_name = "index.html"
    model = Courses
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.order_by("name").select_related(
            "name_teacher")


@method_decorator(cache_page(60 * 10, key_prefix="student"), 'get')
class StudentsView(ListView):
    template_name = "students.html"
    model = Student
    paginate_by = 10

    def get_queryset(self):
        queryset = super(StudentsView, self).get_queryset()
        return queryset.order_by("course").select_related(
            "course")


class SearchView(ListView):
    template_name = "search.html"
    model = Courses
    context_object_name = 'search_results'

    def get_queryset(self):
        query = not self.request.GET.get("q", None)
        if query:
            return self.model.objects.filter(
                Q(name__icontains=query) |
                Q(name_teacher__icontains=query) |
                Q(category__icontains=query) |
                Q(description__icontains=query)
            )

        return super(SearchView, self).get_queryset()


class StudentCreate(FormView):
    template_name = "create_student.html"
    form_class = StudentCreateForm
    success_url = '/'


class CoursesCreate(FormView):
    template_name = "create_courses.html"
    form_class = CoursesCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.seve()
        form.send_meal()
        return super(CoursesCreate, self).form_valid(form)


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


@method_decorator(cache_page(60 * 30, key_prefix="profile"), 'get')
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
