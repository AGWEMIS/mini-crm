from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from . forms import AgentModelForm


class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        request_user_orginasation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_orginasation)


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents-list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    model = Agent

    def get_queryset(self):
        request_user_orginasation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_orginasation)


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    context_object_name = 'agent'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents-list')

    def get_queryset(self):
        request_user_orginasation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_orginasation)


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    model = Agent
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agents-list')

    def get_queryset(self):
        request_user_orginasation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_orginasation)
