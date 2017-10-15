from django.conf.urls import url

from . import views
from .views import IndexView

app_name = 'weather'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^(?P<location_name>(.*)+)/$', views.detail, name='detail'),
]