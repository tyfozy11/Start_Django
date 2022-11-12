from django.urls import path
from core import views

urlpatterns = [
    path("courses_create/", views.CoursesCreate.as_view(), name='courses_create'),
    path("student_create/", views.StudentCreate.as_view(), name='student_create'),
    path("change/<int:course_id>/courses/", views.ChangeCourses.as_view(), name='change_courses'),
    path("change/<int:student_id>/student/", views.ChangeStudent.as_view(), name='change_student'),


]
