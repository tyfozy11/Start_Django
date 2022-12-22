from rest_framework.viewsets import ModelViewSet
from api.serializers import StudentSerializer, TeacherSerializer, GroupSerializer
from core.models import Student, Teacher, Group


class StudentListView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class TeacherListView(ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()


class GroupListView(ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()
