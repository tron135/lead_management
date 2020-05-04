from django.shortcuts import render, redirect
from .models import Lead

# Create your views here.

def home(request):
    return render(request, 'initial.htm')

def lead(request):
    if request.POST:
        fromDate = request.POST.get('from')
        toDate = request.POST.get('to')
        system = request.POST.getlist('dropdown')
        filtered = Lead.objects.filter(creation_time__range=(fromDate, toDate))
        leads = filtered.values(*system)

    print(leads)
    context = {'leads':leads}

    return render(request, 'lead/lead.htm', context)
