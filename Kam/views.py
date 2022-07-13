
from urllib.request import Request
from django.shortcuts import render
from . forms import Mera
from . models import Info
# Create your views here.


def data (request):
    data = Mera
    if request.method == 'POST' :
        data = Mera(request.POST)
        if data.is_valid():
            F_name = data.cleaned_data['F_name']
            L_name = data.cleaned_data['L_name']
            Email  = data.cleaned_data['Email']


            Info.objects.create(F_name=F_name,L_name=L_name,Email = Email)
    else :
        data = Mera
    return render(request,'logic.html' ,context = {"form" : data})