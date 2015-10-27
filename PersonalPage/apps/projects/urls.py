from django.conf.urls import url
from projects.views import ProjectView, CategoryView

urlpatterns = [
    url(r'^(?P<category_sname>[a-zA-Z-0-9]*)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_sname>[a-zA-Z-0-9]*)/(?P<project_sname>[a-zA-Z-0-9]*)/$', ProjectView.as_view(), name='project'),
]
