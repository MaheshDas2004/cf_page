from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import random
from .models import Profile
def signup(request):
    if request.method == "POST":
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        
        email = request.POST.get("email")
        password = request.POST.get("password")
        cf_pass = request.POST.get("confirm_password")
        college=request.POST.get("college")
        username = f"{email.split('@')[0]}_{random.randint(1000, 9999)}"

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/signup.html", {
                'error': "Email already registered.",
                'first_name': f_name,
                'last_name': l_name,
                'email': email,
                'college':college
            })

        if password != cf_pass:
            return render(request, "accounts/signup.html", {
                'error': "Passwords do not match.",
                'first_name': f_name,
                'last_name': l_name,
                'email': email,
                'college':college
            })

        if len(password) < 6:
            return render(request, "accounts/signup.html", {
                'error': "Password must be at least 6 characters.",
                'first_name': f_name,
                'last_name': l_name,
                'email': email,
                'college':college
            })

        
        user=User.objects.create_user(username=username,first_name=f_name,last_name=l_name, email=email, password=password)
        profile=Profile.objects.create(user=user,college=college)
        login(request,user)
        return redirect("home")
        print(request.POST)

    return render(request, "accounts/signup.html")

def login_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            is_user= User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request,"accounts/login.html",{'error':"email not registered"})
        
        user = authenticate(request, username=is_user.username, password=password)
        
        if(user is not None):
            login(request,user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid password."
            })
    return render(request, "accounts/login.html")

def profile_panel(request):
    return render(request,"accounts/profile.html")

def logout_user(request):
    logout(request)
    return redirect("home")