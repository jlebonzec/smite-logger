from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    resolve_url
)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from logger.forms import MatchForm


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Hey, {}!".format(request.user.username))
    else:
        return HttpResponse("Boo, I don't know you!")


def connect(request):
    auth_form = AuthenticationForm()
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.username
            password = auth_form.password
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponseRedirect(resolve_url('index'))
    return HttpResponse(auth_form)


@login_required
def log(request):
    match_form = MatchForm()
    if request.method == "POST":
        match_form = MatchForm(request.POST)
        if match_form.is_valid():
            match_form.save()
            return HttpResponseRedirect(resolve_url('index'))

    return render(request, 'logger/log.html', {
        'log_form': match_form,
    })
