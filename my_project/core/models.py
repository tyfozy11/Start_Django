from django.db import models
from my_project import settings


class Name(models.Model):
    name = models.CharField(max_length=255, unique=True)

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
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(max_length=200)
    group = models.ForeignKey("core.Group", on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey("core.Courses", on_delete=models.SET_NULL, null=True)


class Courses(Name):
    category = models.ForeignKey("core.Category", on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    name_teacher = models.ForeignKey("core.Teacher", on_delete=models.SET_NULL, null=True)
    short_list_of_course_theses = models.TextField()


class Category(Name):
    pass


class ExchangeRates(models.Model):
    bank = models.CharField(max_length=255, unique=True)
    currency_name_1 = models.CharField(max_length=255, default=True)
    currency_name_2 = models.CharField(max_length=255, default=True)
    rate_buy = models.DecimalField(max_digits=7, decimal_places=4, default=True)
    rate_sell = models.DecimalField(max_digits=7, decimal_places=4, default=True)

    def __str__(self):
        return f"{self.bank } {self.currency_name_1}"
