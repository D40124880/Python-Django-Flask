from django.conf.urls import url
from . import views  # this line is new!

urlpatterns = [
    url(r'^$', views.index),   # this line has changed
    url(r'^test$', views.test),  # start with ^test and end with test$...
]