from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=200)
    group = models.ForeignKey("core.Group", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=200)
    group = models.ForeignKey("core.Group", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
