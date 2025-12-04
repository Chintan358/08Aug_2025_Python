from django.shortcuts import render,redirect
from myapp.models import Student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_student(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    if not id : 
        Student.objects.create(name=name, email=email, age=age)
        return render(request, 'home.html',{'success':'Student registered successfully',})
    else : 
        st = Student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.age = age
        st.save()
        return render(request, 'home.html',{'success':'Student update successfully',})


def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})

def delete_student(request):
    id =  request.GET.get("id")
    st = Student.objects.get(pk=id)
    st.delete()
    return redirect("display")

def edit_student(request):
    id =  request.GET.get("id")
    st = Student.objects.get(pk=id)
    return render(request,"home.html",{"st":st})