import logging

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from view.models import Weatherdata, Weatherstation


def index(request):
    wd = Weatherdata.objects.select_related('user__weatherdata').all().order_by('-timestamp')
    return render_to_response('view/index.html', {'weatherdata': wd})


def detail(request, ws_id):
    try:
        ws = Weatherstation.objects.get(id=ws_id)
        wd = Weatherdata.objects.filter(weatherstation_id=ws.id).all().order_by('-timestamp')
    except Weatherstation.DoesNotExist:
        raise Http404
    return render_to_response('view/detail.html', {'weatherdata': wd})


def user_ws(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        weatherstation = Weatherstation.objects.select_related('user__weatherdata').filter(user_id=user_id).all()
        weather_dict = {}
        if Weatherstation.objects.filter(user_id=user_id):
            for ws in weatherstation:
                wd = Weatherdata.objects.select_related('weatherstation__weatherdata').filter(weatherstation_id=ws.id).\
                    all().order_by('-timestamp')
                weather_dict[ws] = wd
        else:
            return HttpResponse('Keine Wetterstationen verfügbar')
    except User.DoesNotExist:
        raise Http404
    context = {'weather_dict': weather_dict, 'user': user}
    return render_to_response('view/user_ws.html', context)

@method_decorator(csrf_exempt)
def save_wd(request):
    log = logging.getLogger()
    log.debug(request)
    if request.method == 'POST':
        humidity = request.POST.get("humidity")
        temperature = request.POST.get("temperature")
        altitude = request.POST.get("altitude")
        air_pressure = request.POST.get("air_pressure")
        lightness = request.POST.get("lightness")
        weatherstation_id = request.POST.get("weatherstation_id")
        user_id = request.POST.get("user_id")
        weatherdata = Weatherdata(humidity=humidity, temperature=temperature, altitude=altitude, air_pressure=air_pressure, lightness=lightness, weatherstation_id=weatherstation_id, user_id=user_id)
        weatherdata.save()

        return HttpResponse(weatherdata)

