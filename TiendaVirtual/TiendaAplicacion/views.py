from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")