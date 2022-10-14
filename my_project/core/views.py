from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView
from core.models import Group, Teacher, Student, Courses, Category
from core.forms import StudentCreateForm, CoursesCreateForm


class IndexView(ListView):
    template_name = "index.html"
    model = Courses

    # paginate_by = 10
    #
    # def get_queryset(self):
    #     queryset = super(IndexView, self).get_queryset()
    #     return queryset.order_by("name").select_related(
    #         "name_teacher")

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class SearchView(ListView):
    template_name = "index.html"
    models = Courses

    def get_queryset(self):
        query = not self.request.GET.get("q", None)
        if query:
            return self.models.objects.filter(
                Q(name__iconteins=query) |
                Q(name_teacher__iconteins=query) |
                Q(category__iconteins=query) |
                Q(description__iconteins=query)
            )

        return super(SearchView, self).get_queryset()


class StudentCreate(TemplateView):
    template_name = "create_student.html"

    def get_context_data(self, **kwargs):
        context = super(StudentCreate, self).get_context_data()
        context["form"] = StudentCreateForm()
        return context


class CoursesCreate(TemplateView):
    template_name = "create_courses.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesCreate, self).get_context_data()
        context["form"] = CoursesCreateForm()
        return context
