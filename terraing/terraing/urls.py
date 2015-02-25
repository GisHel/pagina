from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'terraing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('pagina.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    
)
