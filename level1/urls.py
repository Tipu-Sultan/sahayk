from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('students/', views.student_list, name='student_list'),

    path('teacher/<int:teacher_id>/', views.teacher_students, name='teacher_students'),
    path('student/<int:student_id>/', views.student_teachers, name='student_teachers'),

    path('teacher_students/', views.teacher_students_view, name='teacher_students'),
    path('student_teachers/', views.students_teacher_view, name='student_teachers'),

    path('teacher_students/<int:teacher_id>/', views.teacher_students, name='teacher_students'),
    path('student_teachers/<int:student_id>/', views.student_teachers, name='student_teachers'),
    

]
