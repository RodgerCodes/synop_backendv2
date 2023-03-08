from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User, Station
from .forms import NewStation, NewUser, ReassignForm
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

    def form_valid(self, form):
        form.save()
        return redirect('codes:get_stations')
    

@login_required(login_url="/")
def GetObservers(request):
    context = {}
    observers = User.objects.filter(is_superuser=False)
    context['observers'] = observers
    return render(request, 'dashboard/observers.html', context)


@login_required(login_url="/")
def NewObservers(request):
    context = {}
    stations = Station.objects.all()
    context['stations'] = stations

    if request.method == 'POST':
        if request.POST.get('email')  == None or request.POST.get('name') == None:
            messages.error(request, "Please fill in all forms")
        new_password = "Blantyre2023"
        station = Station.objects.get(station_number=int(request.POST.get('station')))
        User.objects.create(
            email = request.POST.get('email'),
            name = request.POST.get('name'),
            station = station,
            is_staff = request.POST.get('is_staff'),
            is_superuser= request.POST.get('is_admin'),
            password = make_password(new_password)
        )

        messages.success(request, f"User with the email {request.POST.get('email')} created with password {new_password}")
        return redirect('accounts:get_observers')
    return render(request, 'dashboard/new_observer.html', context)


@login_required(login_url="/")
def RemoveObserver(request, userId):
    user = User.objects.get(id=userId)
    if not request.user.is_superuser:
        messages.error(request, "Forbidden to perform this operation")
    user.delete()
    messages.success(request, f"User {user.name} deleted successfully")
    return redirect('accounts:get_observers')


@login_required(login_url="/")
def ReassignObserver(request, userID):
    # get current station observer is assigned
    observer_instance = User.objects.get(id=userID)
    form = ReassignForm(instance=observer_instance)

    if request.method == 'POST':
        station_instance = Station.objects.get(id=request.POST.get('station'))
        if observer_instance.station == station_instance:
            messages.error(request, "Observer is already assigned to this station")
        form = ReassignForm(request.POST, instance=observer_instance)
        if form.is_valid():
            form.save(commit=False)
            form.station = station_instance
            form.save()
            messages.success(request, f"Successfully Reassigned {observer_instance.name} to {station_instance.station_name}")
            return redirect('accounts:get_observers')

    return render(request, 'dashboard/assign.html', {'form' : form})