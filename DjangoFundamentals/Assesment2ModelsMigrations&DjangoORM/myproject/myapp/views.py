
from django.http import HttpResponse
from django.db.models import Avg
from .models import Student


def home(request):
    return HttpResponse("Welcome to Django Assessment 2!")


def student_detail(request, student_id):
    return HttpResponse(f"Student ID is: {student_id}")


def adult_students(request):
    students = Student.objects.filter(age__gte=18)

    result = "Adult Students:<br>"

    for student in students:
        result += f"{student.name} - {student.age}<br>"

    return HttpResponse(result)


def average_student_age(request):
    result = Student.objects.aggregate(average_age=Avg('age'))
    average_age = result['average_age']

    return HttpResponse(f"Average student age: {average_age}")
