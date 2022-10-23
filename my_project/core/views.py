from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView
from core.models import Courses, Category
from core.forms import StudentCreateForm


class IndexView(ListView):
    template_name = "index.html"
    model = Courses
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.order_by("name").select_related(
            "name_teacher")

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


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
