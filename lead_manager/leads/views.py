from django.shortcuts import render, redirect
from .models import Lead, FollowUp

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

        if 'followup' in request.POST.getlist('dropdown'):
            names = filtered.values('name').values_list('id')
            out = [item for t in names for item in t]
            print(out)

            if len(names) != 0:
                followup = FollowUp.objects.filter(lead_name_id__in=out).order_by('lead_name').values()
            else:    
                followup = FollowUp.objects.all().order_by('lead_name').values()
        else:
            followup = {}

    context = {'leads':leads, 'followup':followup}

    return render(request, 'lead/lead.htm', context)
