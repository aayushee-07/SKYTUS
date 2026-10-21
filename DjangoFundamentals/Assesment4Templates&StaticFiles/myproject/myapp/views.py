
from django.http import HttpResponse
from django.db.models import Avg
from django.shortcuts import render
from .models import Student
from .models import Book
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy


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

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')


def home(request):
    items = [
        {"name": "Python", "available": True},
        {"name": "Django", "available": True},
        {"name": "JavaScript", "available": False},
    ]

    return render(request, "myapp/home.html", {"items": items})