from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login , {'template_name': 'qa/login.html'}, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^question/(?P<id>[^/]+)/$', views.question, name='question'),
    url(r'^ask', views.ask, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.home, name='new'),
    url(r'^answer/$', views.answer, name='answer'),
]
