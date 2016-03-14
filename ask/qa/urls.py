from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<id>[^/]+)/$', views.question, name='question'),
    url(r'^ask', views.test, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.home, name='new'),
]
