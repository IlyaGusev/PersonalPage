from django.conf.urls import url
from games.views import GameView

urlpatterns = [
    url(r'^(?P<game_sname>[a-zA-Z-0-9]*)/$', GameView.as_view(), name='game'),
]