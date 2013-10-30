from django.conf.urls import patterns, include, url

from timer.views import hello, current_datetime, hours_ahead
from views import home, thankyou

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplewebsiteEXAMPLE.views.home', name='home'),
    # url(r'^simplewebsiteEXAMPLE/', include('simplewebsiteEXAMPLE.foo.urls')),

    #timer.views:
    url(r'hello/$', hello, name="hello"),
    url(r'^time/$', current_datetime, name="timer"),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead, name="timeplus"),

    #views.py
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

    #contact app
    url(r'^contact/', 'contact.views.contact'),
   
    #view.py 
    url(r'^home/$', home, name="home"),
    url(r'^thankyou/$', thankyou, name="thankyou"),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
