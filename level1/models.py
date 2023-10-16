from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Certificate for {self.student.name} from {self.teacher.name}'
