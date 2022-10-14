from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Group(Name):
    pass


class Teacher(Name):
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=200)
    group = models.ForeignKey("core.Group", on_delete=models.SET_NULL, null=True)


class Student(Name):
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=200)
    group = models.ForeignKey("core.Group", on_delete=models.SET_NULL, null=True)


class Courses(Name):
    category = models.ForeignKey("core.Category", on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    name_teacher = models.ForeignKey("core.Teacher", on_delete=models.SET_NULL, null=True)
    short_list_of_course_theses = models.TextField()


class Category(Name):
    pass
