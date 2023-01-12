from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView

# Create your views here.

class taskList(ListView):
    model = Task
    context_object_name = 'tasks'


class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'