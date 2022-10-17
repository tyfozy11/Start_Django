from django.views.generic import TemplateView, ListView
from core.models import Courses, Category


class IndexView(ListView):
    template_name = "index.html"
    model = Courses
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.order_by("name").select_related(
            "name_teacher").filter(name_teacher_id__gt=0)

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context
