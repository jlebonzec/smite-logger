from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /logger
    url(r'^$', views.index, name='index'),
    url(r'^log', views.log, name='log')
]
