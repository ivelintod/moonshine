from django.conf.urls import url
from beer import views

whiskey_list = views.WhiskeyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

whiskey_detail = views.WhiskeyViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    url(r'^beer/$', views.BeerDetail.as_view(), name='beer-post'),
    url(r'^beer/(?P<pk>.*)/$', views.BeerDetail.as_view(), name='beer-get'),
    url(r'^whiskey/$', whiskey_list, name='whiskey-list'),
    url(r'^whiskey/(?P<pk>.*)/$', whiskey_detail, name='whiskey-detail'),
]

beer_api_urls = urlpatterns
