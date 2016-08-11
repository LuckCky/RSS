from django.shortcuts import render_to_response
from django.http import HttpResponse
from lenta_rss.lenta.lrss.models import News

def search_form(request):
    return render_to_response('search_form.html')

def search(request):#from and till
    if 'from' in request.GET and request.GET['from'] and 'till' in request.GET and request.GET['till']:
        f = request.GET['from']
        t = request.GET['till']
        news = Book.objects.filter(Date__icontains=f)
        return render_to_response('search_results.html', {'News': news, 'query': f, 'query2': t})
    else:
        return HttpResponse('Введите поисковый запрос.')
