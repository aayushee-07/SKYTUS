from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('adult-students/', views.adult_students, name='adult_students'),
    path('average-age/', views.average_student_age, name='average_age'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/add/', views.BookCreateView.as_view(), name='book_create'),
]