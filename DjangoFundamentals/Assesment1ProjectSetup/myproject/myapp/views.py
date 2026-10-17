from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Django Assessment 1!")

def student_detail(request, student_id):
    return HttpResponse(f"Student ID is: {student_id}")