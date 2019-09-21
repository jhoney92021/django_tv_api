from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows/details/(?P<showID>\d+)/delete$', views.showDelete),
    url(r'^shows/details/(?P<showID>\d+)/edit/process$', views.showEditProcess),
    url(r'^shows/details/(?P<showID>\d+)/edit$', views.showEdit),
    url(r'^shows/details/(?P<showID>\d+)$', views.showDetails),
    url(r'^shows/new/process$', views.newShowProcess),
    url(r'^shows/new$', views.newShow),
    url(r'^shows$', views.shows),
    url(r'^$', views.index),
]