from django.shortcuts import (
    render,
    HttpResponse,
    HttpResponseRedirect,
    resolve_url
)
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm

from dal import autocomplete

from logger.models import God
from logger.forms import MatchForm


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Hey, {}!".format(request.user.username))
    else:
        return HttpResponse("Boo, I don't know you!")


def login_view(request):
    auth_form = AuthenticationForm()
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        print("hi")
        if auth_form.is_valid():
            print("is valid")
            username = auth_form.username
            password = auth_form.password
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, username)
                return HttpResponseRedirect(resolve_url('index'))
        print(auth_form)
    return render(request, 'logger/login.html', {
        'login_form': auth_form
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(resolve_url('index'))


@login_required
@permission_required('logger.add_match', raise_exception=True)
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


#  - Autocomplete views -
class GodAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return God.objects.none()
        qs = God.objects.all().order_by('name')

        if self.q:
            pattern = (
                Q(name__icontains=self.q) |
                Q(pantheon__name__iexact=self.q) |
                Q(role__name__iexact=self.q) |
                Q(role__damage__iexact=self.q) |
                Q(role__attack__iexact=self.q)
            )
            qs = qs.filter(pattern)

        return qs
