from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Login
from .forms import SignupForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Login.objects.get(email=email) 
            if user.check_password(password):     
                request.session['user_id'] = user.id
                messages.success(request, f"Welcome {user.full_name}!")
                return render(request, 'success.html', {'username': user.full_name})
            else:
                messages.error(request, "Incorrect password")
        except Login.DoesNotExist:
            messages.error(request, "User does not exist")
    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully! login.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def welcome_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Login.objects.get(id=user_id)
        return render(request, 'success.html', {'username': user.full_name})
    else:
        return redirect('login')