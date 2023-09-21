from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("ehmail")
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email)

        login(request, user)

        return redirect('index')

    return render(request, 'account/signup.html')


def login_u(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
        return render(request, 'account/login.html')




def logout_u(request):
    logout(request)
    return redirect('index')
