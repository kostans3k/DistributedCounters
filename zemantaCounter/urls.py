from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zemantaCounter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'counters.views.home', name='home'),
    url(r'^counters/$', 'counters.views.counters_list', name='counters_list'),
    url(r'^counters/add/$', 'counters.views.add_counter'),
    url(r'^counters/(?P<counter_id>\d+)/$', 'counters.views.counter_detail', name='counter_detail'),
    url(r'^counters/(?P<counter_id>\d+)/increase/$', 'counters.views.counter_increase'),
    url(r'^counters/(?P<counter_id>\d+)/reset/$', 'counters.views.counter_reset'),
)
