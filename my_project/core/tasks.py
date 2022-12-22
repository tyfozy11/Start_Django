import datetime
from my_project.celery import app
from django.core.mail import send_mail
from core.models import Student, Courses


@app.task
def alert_of_new_course(data):
    emails = Student.objects.all().values_lisr('email', flat=True)
    message = f" A new course has been added {data['name']}"
    for email in emails:
        send_mail(
            subject='A new course has been added',
            from_email='admin@youк_skool.com',
            message=message,
            recipient_list=[email]
        )


@app.task
def mailing():
    today = datetime.datetime.now().date()
    emails = Student.objects.all().values_lisr('email', flat=True)
    course = Courses.objects.filter(created_at__contains=today).values_lisr('name', flat=True)
    message = f"Visit our site, new courses appeared there:{','.join(course)}"

    for email in emails:
        send_mail(
            subject='A new course has been added',
            from_email='admin@youк_skool.com',
            message=message,
            recipient_list=[email])
