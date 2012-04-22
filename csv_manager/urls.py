from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csv_manager.views.home', name='home'),
    # url(r'^csv_manager/', include('csv_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^$','files_manager.views.file_list'),
    url(r'^upload/$','files_manager.views.file_upload'),
    url(r'^file_view/(\d+)/$','files_manager.views.file_view'),
)