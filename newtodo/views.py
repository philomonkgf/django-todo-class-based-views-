
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import NewTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

from django.contrib import messages
from django.urls import reverse_lazy
# class
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView

from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View





# Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model = NewTask
    template_name = 'newtodo/index.html'
    context_object_name = 'task'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count'] = context['task'].filter(completed = False).count() 
        return context 
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = NewTask
    template_name = 'newtodo/detail.html'
    context_object_name = 'task'
    
class Taskcreate(LoginRequiredMixin,CreateView):
    model = NewTask
    template_name = 'newtodo/create.html'
    fields = ['task',]
    success_url = reverse_lazy('index')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(Taskcreate,self).form_valid(form)
    
class DeleteTask(LoginRequiredMixin,DeleteView):
    model = NewTask
    template_name = 'newtodo/delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('index')
    
    
class EditTask(LoginRequiredMixin,UpdateView):
    model=NewTask
    template_name = 'newtodo/edit.html'
    fields = ['task','completed',]
    success_url = reverse_lazy('index')
    
class CustomLoginView(LoginView):
    template_name = 'newtodo/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
   
    
    def post(self,request, *args,**kwargs):
        username=request.POST['username']
        password=request.POST['password']
        form = authenticate(request,username=username,password=password)
        if form is not None:
            login(request,form)
            return redirect('index')
        messages.error(self.request,'Invalid username or password')
        return super().form_invalid(form)
  
    
    
class Registerpage(FormView):
    template_name = 'newtodo/registerpage.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Registerpage,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(Registerpage,self).get(*args,**kwargs)
    
    

class Passwordchange(LoginRequiredMixin,PasswordChangeView):
    template_name = 'newtodo/passwordchange.html'
    success_url = reverse_lazy('passworddone')
    
    
   
class PasswordDone(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'newtodo/passworddone.html'
    
    