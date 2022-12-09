from api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'students', views.StudentListView, basename='students')
router.register(r'teachers', views.TeacherListView, basename='teachers')
router.register(r'groups', views.GroupListView, basename='groups')

urlpatterns = [
              ] + router.urls
