#always do the following
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^show/(?P<number1>\d+)$', views.show),
    url(r'^(?P<number2>\d+)/edit$', views.edit),
    url(r'^(?P<number3>\d+)/destroy$', views.destroy),
]