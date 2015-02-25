from django.conf.urls import patterns, url
from pagina import views,feed
from django.conf import settings

urlpatterns = patterns('',
                       #url(r'^$', views.first_view, name='first-view'),
                       url(r'^feed/$', feed.LatestPosts(), name="feed"),
                       url(r'^$', views.BlogIndex.as_view(), name="index"),
                       url(r'^(?P<pk>\d+)$', views.BlogDetail.as_view(), name="entry-detail"),                      
                      )
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

   )


