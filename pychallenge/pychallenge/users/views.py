from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from pychallenge.users.models import About


# Create your views here.
class AboutMeView(LoginRequiredMixin, DetailView):
    """CBV to show the about me for the logged in user"""
    model = About
    template_name = "pages/about.html"

    def get_object(self):
        obj = About.objects.filter(user=self.request.user).get_published().first()
        return obj
