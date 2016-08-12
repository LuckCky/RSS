from django.shortcuts import render_to_response
from django.http import HttpResponse
from lenta_rss.lenta.lrss.models import News
import datetime

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'from' in request.GET and request.GET['from'] and 'till' in request.GET and request.GET['till']:
        f = request.GET['from']
        t = request.GET['till']
        news = News.objects.filter(date__range=[f, t])
        return render_to_response('search_results.html', {'News': news, 'from': f, 'till': t})
    else:
        return HttpResponse('Введите поисковый запрос.')
