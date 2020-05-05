from django.shortcuts import render, redirect
from .models import Lead, FollowUp

# Create your views here.

def home(request):
    return render(request, 'initial.htm')

def lead(request):
    if request.POST:
        fromDate = request.POST.get('from')
        toDate = request.POST.get('to')
        system = ['id'] + request.POST.getlist('dropdown')
        print(system)
        if 'followup' in system:
            system.remove('followup')

        filtered = Lead.objects.filter(creation_time__range=(fromDate, toDate))
        leads = filtered.values(*system)

        if 'followup' in request.POST.getlist('dropdown'):
            # names = filtered.values('name').values_list('id', flat=True)
            for lead in leads:
                names = FollowUp.objects.filter(lead_name_id=lead['id']).values()
                lead['followup'] = list(names)
        print(leads)

    context = {'leads':leads, 'lof': len(system)}

    return render(request, 'lead/lead.htm', context)
