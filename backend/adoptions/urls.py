
from django.conf.urls import patterns, url
from adoptions import views


urlpatterns = patterns('',

    # Dogs
    url(r'^dogs/$',                    views.DogList.as_view(),      name='dog-list'),
    url(r'^dogs/(?P<pk>[0-9]+)/$',     views.DogDetail.as_view(),    name='dog-detail'),

    # Broods
    url(r'^broods/$',                  views.BroodList.as_view(),    name='brood-list'),
    url(r'^broods/(?P<pk>[0-9]+)/$',   views.BroodDetail.as_view(),  name='brood-detail'),
)