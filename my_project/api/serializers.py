from abc import ABC

from rest_framework import serializers
from core.models import Student, Teacher, Group


class NameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class StudentSerializer(serializers.ModelSerializer):
    group = NameSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    group = NameSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class GroupSerializer(NameSerializer):

    class Meta:
        model = Group
        fields = "__all__"
