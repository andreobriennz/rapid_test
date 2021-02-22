import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import PerformanceData

def index(request):
    items = PerformanceData.objects.order_by('-pub_date')[:50]
    return render(request, 'main/index.html', {'items': items})

def detail(request, performance_data_id):
    item = get_object_or_404(PerformanceData, pk=performance_data_id)
    data = json.loads(item.data)['log']
    page = data['pages'][0]['title']
    return render(request, 'main/detail.html', {'item': item, 'page': page, 'entries': data['entries']})
