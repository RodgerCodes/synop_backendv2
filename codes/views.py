from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Data, synop
from datetime import datetime


@login_required(login_url="/")
def GetDashboard(request):
    context = {}
    today = datetime.today()
    synops = synop.objects.filter(created__year=today.year, created__month=today.month, created__day=today.day)[0:6]
    context['synops'] = synops
    return render(request, 'dashboard/index.html', context)