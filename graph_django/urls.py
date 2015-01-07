from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('graphs.urls')),
)
