from django.conf.urls import url
from entries.views import EntryView

urlpatterns = [
    url(r'^(?P<entry_sname>[a-zA-Z-0-9]*)/$', EntryView.as_view(), name='entry'),
]