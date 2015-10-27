from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render


def index(request):
    return HttpResponseRedirect(reverse('entries:entry', args=('home',)))


def game(request):
    return render(request, 'game.html')