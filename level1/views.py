from django.shortcuts import render, get_object_or_404
from .models import Teacher, Student

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'level1/teacher_list.html', {'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'level1/student_list.html', {'students': students})


def teacher_students(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    students = teacher.student_set.all()
    return render(request, 'level1/teacher_students.html', {'teacher': teacher, 'students': students})

def student_teachers(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    teachers = student.teachers.all()
    return render(request, 'level1/student_teachers.html', {'student': student, 'teachers': teachers})


def teacher_students_view(request):
    return render(request, 'level1/teacher_students.html')

def students_teacher_view(request):
    return render(request, 'level1/student_teachers.html')
