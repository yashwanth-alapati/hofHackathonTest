from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        
        try:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'signup.html')
            
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'signup.html')
            
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # Create user profile
            user_profile = UserProfile.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            
            # Log the user in
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to home page
            
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')