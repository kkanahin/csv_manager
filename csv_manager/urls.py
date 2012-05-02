from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
#    (r'^static/(?P.*)$', 'django.views.static.serve',{'document_root':'settings.MEDIA_ROOT'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^category/([\w-]+)?$','files_manager.views.file_list',name="file_list"),
    url(r'^$','files_manager.views.file_list',name="file_list"),
    url(r'^upload/$','files_manager.views.file_upload',name="file_upload"),
    url(r'^file_view/(\d+)/$','files_manager.views.file_view',name="file_view"),
)
urlpatterns += staticfiles_urlpatterns()