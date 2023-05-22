from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

from .models import User1


def log(request):
    return render(request, 'home.html')


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('register')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        birthdate = request.POST.get('birthdate')

        if username == '' or password == '' or firstname == '' or lastname == '' or gender == '' or contact == '' or birthdate == '':
            messages.error(request, "All Feilds Are Mandatory")
        elif password != cpassword:
            messages.error(request, "Password Didn't Match")
        else:
            person = User1(username=username, first_name=firstname, last_name=lastname, password=password,
                           birthdate=birthdate, contact=contact, gender=gender)
            person.save()
            redirect('/register')
    return render(request, 'register.html')
