from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/<int:teacher_id>/<int:student_id>/', views.generate_certificate, name='generate_certificate'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('student/', views.student_view, name='student'),
]
