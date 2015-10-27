from django.views.generic import DetailView
from entries.models import Entry


class EntryView(DetailView):
    model = Entry
    template_name = "entry.html"
    context_object_name = 'entry'
    slug_field = 'sname'
    slug_url_kwarg = 'entry_sname'