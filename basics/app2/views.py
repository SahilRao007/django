from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("this is the home page for class based views")

# class based views
from django.views.generic.edit import CreateView
from .models import Data2

class create(CreateView):
    model=Data2
    fields=['title','content']
    template_name='create.html'
    success_url='/app2/create'
from django.views.generic.list import ListView

class listing(ListView):
    model=Data2
    template_name='list.html'
    context_object_name='values'
    
from django.views.generic.detail import DetailView

class detailed(DetailView):
    model=Data2
    template_name='detail.html'
    context_object_name='values'
    

from django.views.generic.edit import DeleteView

class deleting(DeleteView):
    model=Data2
    template_name='delete.html'
    success_url='/app2/list'