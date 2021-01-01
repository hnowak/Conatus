from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
