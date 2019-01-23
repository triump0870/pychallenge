from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.shortcuts import get_object_or_404
from pychallenge.users.models import About
from django import http
from pychallenge.users.forms import AboutForm


# Create your views here.
class AboutMeView(LoginRequiredMixin, DetailView):
    """CBV to show the about me for the logged in user"""
    model = About
    template_name = "pages/about.html"

    def get_object(self):
        obj = About.objects.filter(user=self.request.user).get_published().first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AboutForm()
        return context
