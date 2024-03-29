"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(template_name='index.html'), name='home'),
    path("search/", views.SearchView.as_view(template_name='search.html'), name='search'),
    path("login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='login.html'), name='logout'),
    path("students/", views.StudentsView.as_view(), name='students'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("", include(('core.urls', 'core'), namespace='data_correction')),
    path("api/", include(('api.urls', 'api'), namespace='api')),
    path('__debug__/', include('debug_toolbar.urls')),
]
