from django.shortcuts import render_to_response
from django.http import HttpResponse
from lenta_rss.lenta.lrss.models import News

def search_form(request):
    rubrics = News.objects.values('rubric').distinct()
    return render_to_response('search_form.html', rubrics)

def search(request):
    if 'from' in request.GET and request.GET['from'] and 'till' in request.GET and request.GET['till']:
        f = request.GET['from']
        t = request.GET['till']
        news = News.objects.filter(date__range=[f, t])
        return render_to_response('search_results.html', {'News': news, 'from': f, 'till': t})
    else:
        return HttpResponse('Введите поисковый запрос.')

# if __name__ == '__main__':
#     from django.conf import settings
#     settings.configure()
#     rubrics = News.objects.values('rubric').distinct()
#     print(rubrics)
