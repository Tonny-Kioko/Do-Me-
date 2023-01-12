from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm





# Create your views here.
#Login View
class userLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


#registration View
class userRegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm    
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            LoginView(self.request, user)
        return super(userRegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect ('tasks')
        return super(userRegisterPage, self).get(*args, **kwargs)


#CRUD Classes

class taskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        polished =  super().get_context_data(**kwargs)
        polished['tasks'] = polished['tasks'].filter(user = self.request.user)
        polished['count'] = polished['tasks'].filter(complete = False).count()

        search_tasks = self.request.GET.get('search') or "Search for Tasks"
        if search_tasks:
            polished['tasks'] = polished['tasks'].filter(title__icontains= search_tasks)

        polished['search_tasks'] = search_tasks
        
        return polished

    


class taskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class taskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(taskCreate, self).form_valid(form)


class taskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class taskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('tasks')  


