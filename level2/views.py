from django.shortcuts import render, get_object_or_404
from level1.models import Teacher, Student, Certificate
from django.shortcuts import render

def generate_certificate(request, teacher_id, student_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    student = get_object_or_404(Student, pk=student_id)

    # Create a certificate for the teacher-student pair
    certificate = Certificate.objects.create(teacher=teacher, student=student)

    return render(request, 'generate_certificate.html', {'certificate': certificate})


def teacher_view(request):
    return render(request, 'level2/teacher.html')

def student_view(request):
    return render(request, 'level2/student.html')


