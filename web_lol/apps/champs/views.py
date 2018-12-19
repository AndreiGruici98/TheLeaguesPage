from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Champion


class ChampionListView(ListView):
    model = Champion
    template_name = "champs/champion_list.html"


class ChampionDetailView(DetailView):
    model = Champion
    template_name = "champs/champion_detail.html"


class ChampionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Champion
    template_name = "champs/champion_create_update.html"
    fields = ['name', 'alias', 'quote', 'biography', 'role', 'youtube_video_id', 'avatar', 'wallpaper']
    success_url = "/"
    success_message = "The Champion was added!"


class ChampionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Champion
    template_name = "champs/champion_create_update.html"
    fields = ['name', 'alias', 'quote', 'biography', 'role', 'youtube_video_id', 'avatar', 'wallpaper']
    success_url = "/"
    success_message = "The Champion was updated!"


class ChampionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Champion
    template_name = "champs/champion_delete.html"
    success_url = "/"
    success_message = "The Champion was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ChampionDeleteView, self).delete(request, *args, **kwargs)
