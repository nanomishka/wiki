from django.conf.urls import patterns, url

from wikitest import views

urlpatterns = patterns('',
    url(r'^edit/(?P<url>\w{0,50})', views.edit, name='edit'),
    url(r'^save', views.save, name='save'),
    url(r'^add', views.add, name='add'),
    url(r'^(?P<url>\w{0,50})', views.index, name='index'),
)