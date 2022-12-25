from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def GetDashboard(request):
    return render(request, 'dashboard/index.html')