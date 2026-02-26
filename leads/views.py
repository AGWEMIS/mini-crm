from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing_page.html"


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadModelForm
    template_name = "leads/lead_create.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:leads-list")

    def form_valid(self, form):
        send_mail(
            subject="Lead Created",
            message="Lead was successfully created!",
            from_email="test@test.com",
            recipient_list=['test@test.com'],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadModelForm
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:leads-list")


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Lead.objects.all()
    context_object_name = "lead"
    template_name = "leads/lead_delete.html"

    def get_success_url(self):
        return reverse("leads:leads-list")