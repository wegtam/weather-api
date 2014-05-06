from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import *


def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('../ws/%d' % user.id)
        else:
            err = "Dein Account is nicht gültig, bitte kontaktieren Sie den Administrator"
    else:
        err = 'Dein Benutzername und/oder dein Passwort stimmen nicht überein.'
    return render_to_response('auth/login.html', context_instance=RequestContext(request, {'err': err}))


# Create your views here.
