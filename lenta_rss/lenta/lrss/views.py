from django.shortcuts import render_to_response
from django.http import HttpResponse

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'Вы искали: {0}'.format(request.GET['q'])
    else:
        message = 'Вы отправили пустую форму!'
    return HttpResponse(message)
