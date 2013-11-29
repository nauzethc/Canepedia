
from django.conf.urls import patterns, url
from database import views


urlpatterns = patterns('',

    # Groups
    url(r'^groups/$',                  views.FCIGroupList.as_view(), name='group-list'),

    # Families
    url(r'^families/$',                views.FamilyList.as_view(),   name='family-list'),
    url(r'^families/(?P<pk>[0-9]+)/$', views.FamilyDetail.as_view(), name='family-detail'),

    # Breeds
    url(r'^breeds/$',                  views.BreedList.as_view(),    name='breed-list'),
    url(r'^breeds/(?P<pk>[0-9]+)/$',   views.BreedDetail.as_view(),  name='breed-detail'),
)