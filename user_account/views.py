from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def getHome(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check is user exists
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if not user.is_superuser:
                messages.error(request, "Forbidden to access this appliction")
            else:
                login(request, user)
                messages.success(request, "Login successfully")
                return redirect('codes:dashboard')
        else:
            messages.error(request,"Incorrect username or password")

    return render(request, 'home/login.html')