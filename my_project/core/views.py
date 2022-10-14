from django.views.generic import TemplateView, DetailView, ListView
from core.models import Group, Teacher, Student, Courses, Category


class IndexView(ListView):
    template_name = "index.html"
    models = Courses
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
