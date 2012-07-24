from django.conf.urls.defaults import patterns, include, url
import django_si.app.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',(r'page/$', django_si.app.views.page), (r'page2/$', django_si.app.views.page2), url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
