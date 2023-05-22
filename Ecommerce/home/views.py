from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('register')
    return render(request,'home.html')


def register(request):
    return HttpResponse("Register To be made")