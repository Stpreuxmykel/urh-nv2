from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.


def home(request):
    students =  Student.objects.all()
    return render(request, 'home.html', {'students': students})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,  " Your account have been created successfully ")
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def add_student (request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Student added Successfully ! ")
            return redirect('home')
        form = StudentForm()
        return render(request, 'add_student.html', {'form': form})
    else:
        return render(request, "add_student.html")


def update_student(request, id):
    student= get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "form valid")
            return redirect('home')
    else:
        form=StudentForm(instance=student)
        return render(request, 'update_student.html', {'form': form}) 
    return render(request,'update_student.html', {'form':form})

def delete_student(request, id):
    student= get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Supprimer avec Succes")
    return redirect ('home')
# return render (request, 'delete_student.html')