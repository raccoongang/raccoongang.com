#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Gallery, Photo


class IndexView(generic.ListView):
    template_name = 'top_gallery/index.html'
    context_object_name = 'photo_list'

    def get_queryset(self):
        return Gallery.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Gallery
    template_name = 'top_gallery/detail.html'


class ResultsView(generic.DetailView):
    model = Gallery
    template_name = 'top_gallery/results.html'



