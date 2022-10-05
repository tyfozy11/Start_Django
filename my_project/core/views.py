from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['users']= User.objects.all()
        return context


class ProfileView(DetailView):
    template_name = "profile.html"
    model = User
