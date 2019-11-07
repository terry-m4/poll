from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, RedirectView, UpdateView
from .models import *

# Create your views here.
class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context

class PollVote(RedirectView):
    def get_redirect_url(self,**kwargs):
        opt = Option.objects.get(id=self .kwargs['oid'])
        opt.count +=1
        opt.save()
        return "/poll/{}".format(opt.poll_id)

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']    
    success_url = '/poll/'  

class PollUpdate(UpdateView):
    model = Poll
    fields = ['subject']    
    success_url = '/poll/'  

