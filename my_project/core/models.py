from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=200)
    group = models.ManyToManyField(Group)


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=200)
    group = models.ManyToManyField(Group)
