from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # ex: /logger
    url(r'^$', views.index, name='index'),
    url(r'^login$', login, {'template_name': 'logger/login.html'},
        name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^log', views.log, name='log'),
    url(
        r'^god-autocomplete/$',
        views.GodAutocomplete.as_view(), name='god-autocomplete',
    ),

]
