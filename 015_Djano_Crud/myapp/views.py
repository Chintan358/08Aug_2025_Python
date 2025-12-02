from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_student(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    Student.objects.create(name=name, email=email, age=age)
    return render(request, 'home.html',{'success':'Student registered successfully',})