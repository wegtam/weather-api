from django.http import HttpResponse, Http404

from django.template import Context, loader
from django.shortcuts import render_to_response

from api.models import Weatherdata, Weatherstation


def index(request):
    wd = Weatherdata.objects.all().order_by('-timestamp')
    return render_to_response('api/index.html', {'object_list': wd})


def detail(request, ws_id):
    try:
        ws = Weatherstation.objects.get(id=ws_id)
        wd = Weatherdata.objects.filter(weatherstation_id=ws.id).all().order_by('-timestamp')
    except Weatherstation.DoesNotExist:
        raise Http404
    t = loader.get_template('api/detail.html')
    c = Context({'object_list': wd})
    return HttpResponse(t.render(c))
