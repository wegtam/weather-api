from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from view.models import Weatherdata, Weatherstation, Cities


def index(request):
    wd = Weatherdata.objects.select_related('weatherstation', 'weatherstation__city', 'city__country').all()[:10]
    return render_to_response('view/index.html', {'weatherdata': wd})


def all_wd(request):
    wd = Weatherdata.objects.select_related('weatherstation', 'weatherstation__city', 'city__country').all()
    paginator = Paginator(wd, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        wd = paginator.page(page)
    except (InvalidPage, EmptyPage):
        wd = paginator.page(paginator.num_pages)

    return render_to_response('view/all_wd.html', {'weatherdata': wd})


def detail(request, ws_id):
    try:
        ws = Weatherstation.objects.get(id=ws_id)
        wd = Weatherdata.objects.filter(weatherstation_id=ws.id).all()
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
                    all()
                weather_dict[ws] = wd
        else:
            return HttpResponse('Keine Wetterstationen verfügbar')
    except User.DoesNotExist:
        raise Http404
    context = {'weather_dict': weather_dict, 'user': user}
    return render_to_response('view/user_ws.html', context)


def city_wd(request, city_id):
    try:
        city = Cities.objects.get(id=city_id)
        wd = Weatherdata.objects.select_related('weatherstation', 'weatherstation__city').\
            filter(weatherstation__city=city_id).all()
    except Weatherstation.DoesNotExist:
        raise Http404
    context = {'weatherdata': wd, 'city': city}
    return render_to_response('view/city_wd.html', context)


@method_decorator(csrf_exempt)
def save_wd(request):
    if request.method == 'POST':
        humidity = request.POST.get("humidity")
        temperature = request.POST.get("temperature")
        altitude = request.POST.get("altitude")
        air_pressure = request.POST.get("air_pressure")
        lightness = request.POST.get("lightness")
        weatherstation_id = request.POST.get("weatherstation_id")
        #user_id = request.POST.get("user_id")
        weatherdata = Weatherdata(humidity=humidity, temperature=temperature, altitude=altitude, air_pressure=air_pressure, lightness=lightness, weatherstation_id=weatherstation_id)
        weatherdata.save()

        return HttpResponse(weatherdata)

