from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Station
from .forms import NewStation, NewUser
from django.views.generic import CreateView

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


@login_required(login_url="/")
def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully logged Out")
    return redirect('accounts:login')


class CreateStation(CreateView):
    model = Station
    form_class = NewStation
    template_name = 'dashboard/new_station.html'

