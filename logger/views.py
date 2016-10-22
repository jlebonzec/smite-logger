from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    resolve_url
)
from sqlite3 import IntegrityError

from logger.forms import MatchForm
from logger.models import Match

# Create your views here.


def index(request):
    return HttpResponse("Hey, it's working!")


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
