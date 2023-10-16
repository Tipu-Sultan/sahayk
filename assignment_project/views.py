from django.shortcuts import render

def home(request):
    return render(request, 'assignment_project/home.html')
