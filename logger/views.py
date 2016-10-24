from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    resolve_url
)
from django.contrib.auth import authenticate

from logger.forms import MatchForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Hey, {}!".format(request.user.username))
    else:
        return HttpResponse("Boo, I don't know you!")


def log(request):
    match_form = MatchForm()
    if request.method == "POST":
        match_form = MatchForm(request.POST)
        print(match_form.as_p())
        if match_form.is_valid():
            match_form.save()
            return HttpResponseRedirect(resolve_url('index'))

    return render(request, 'logger/log.html', {
        'log_form': match_form,
    })
