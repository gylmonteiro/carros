from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def create_user_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_user')
    else:
        user_form = UserCreationForm()
    return render(request, 'form_user.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('listCars')
    login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('listCars')
