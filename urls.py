from django.conf.urls.defaults import *

urlpatterns = patterns('nest_bizplan.views',
    url(r'^entry/$', 'entry_form', name='nest_bizplan-entry_form'),
    url(r'^judging-entries/$', 'judge_listing', name='nest_bizplan-judge_listing'),
    url(r'^judging-entries/(?P<entry_id>\w+)/$', 'judge_entry', name='nest_bizplan-judge_entry'),
)
