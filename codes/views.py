from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Data, synop
from user_account.models import Station
from datetime import datetime


@login_required(login_url="/")
def GetDashboard(request):
    context = {}
    today = datetime.today()
    synops = synop.objects.filter(created__year=today.year, created__month=today.month, created__day=today.day)[0:6]
    context['synops'] = synops
    return render(request, 'dashboard/index.html', context)


@login_required(login_url="/")
def GetStations(request):
    context = {}
    met_stations = Station.objects.prefetch_related('station').all()
    context['stations'] = met_stations
    return render(request, 'dashboard/stations.html', context)


@login_required(login_url="/")
def GetSynops(request):
    context = {}
    synops = synop.objects.all()
    context['synops'] = synops
    return render(request, 'dashboard/synops.html')