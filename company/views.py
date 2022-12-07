from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .models import Block, Flat
# from .forms import BlockForm, FlatForm
from .form import BlockForm, FlatForm

class BlockListView(generic.ListView):
    model = Block
    template_name = 'block_list.html'
    context_object_name = 'blocks'


class BlockCreateView(generic.CreateView):
    model = Block
    form_class = BlockForm
    template_name = 'block_form.html'
    success_url = reverse_lazy('block_list')


class BlockDetailView(generic.DetailView):
    model = Block
    template_name = 'block_detail.html'



class FlatListView(generic.ListView):
    model = Flat
    template_name = 'flat_list.html'
    context_object_name = 'flats'


class FlatCreateView(generic.CreateView):
    model = Flat
    form_class = FlatForm
    template_name = 'flat_form.html'
    success_url = reverse_lazy('flat_list')


class FlatDetailView(generic.DetailView):
    model = Flat
    template_name = 'flat_detail.html'