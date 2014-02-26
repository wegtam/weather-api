from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from api.models import Weatherdata, Weatherstation


def index(request):
    wd = Weatherdata.objects.all().order_by('-timestamp')
    return render_to_response('api/index.html', {'weatherdata': wd})


def detail(request, ws_id):
    try:
        ws = Weatherstation.objects.get(id=ws_id)
        wd = Weatherdata.objects.filter(weatherstation_id=ws.id).all().order_by('-timestamp')
    except Weatherstation.DoesNotExist:
        raise Http404
    t = loader.get_template('api/detail.html')
    c = Context({'weatherdata': wd})
    return HttpResponse(t.render(c))


def user_ws(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        weatherstation = Weatherstation.objects.select_related('user__weatherdata').filter(user_id=user_id).all()
        weather_dict = {}
        for ws in weatherstation:
            wd = Weatherdata.objects.select_related('weatherstation__weatherdata').filter(weatherstation_id=ws.id).all()
            weather_dict[ws] = wd

    except User.DoesNotExist:
        raise Http404
    context = {'weather_dict': weather_dict, 'user': user}
    return render_to_response('api/user_ws.html', context)

