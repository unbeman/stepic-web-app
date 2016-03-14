from django.conf.urls import url

from .views import test

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', test, name='login'),
    url(r'^signup/$', test, name='signup'),
    url(r'^question/(?P<id>[^/]+)/$', views.question, name='question'),
    url(r'^ask', test, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.home, name='new'),
]
