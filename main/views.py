import json

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import PerformanceData

def get_time(e):
    return e['time']

def get_size(e):
    return e['response']['content']['size']

def tidy_url(e):
    e['request']['url'] = e['request']['url'].split('?')[0]
    return e


def index(request):
    items = PerformanceData.objects.order_by('-pub_date')[:50]
    return render(request, 'main/index.html', {'items': items})

def detail(request, performance_data_id):
    order_by = request.GET.get('order_by', None)
    item = get_object_or_404(PerformanceData, pk=performance_data_id)
    data = json.loads(item.data)['log']
    page = data['pages'][0]['title']

    entries = data['entries']
    if order_by == 'time':
        entries.sort(key=get_time, reverse=True)
    if order_by == 'size':
        entries.sort(key=get_size, reverse=True)

    entries = map(tidy_url, entries)

    return render(request, 'main/detail.html', {'item': item, 'page': page, 'entries': entries})
