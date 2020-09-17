from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Studio
from .forms import PlaytimeForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    playtime_form = PlaytimeForm()
    return render(request, 'games/detail.html', {
        'game': game, 
        'playtime_form': playtime_form
    })


class GameCreate(CreateView):
    model = Game
    fields = '__all__'


class GameUpdate(UpdateView):
    model = Game
    # Let's disallow renaming of the cat
    fields = '__all__'


class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

def add_playtime(request, game_id):
  form = PlaytimeForm(request.POST)
  if form.is_valid():
    new_playtime = form.save(commit=False)
    new_playtime.game_id = game_id
    new_playtime.save()
  return redirect('detail', game_id=game_id)

class StudioList(ListView):
  model = Studio

class StudioDetail(DetailView):
  model = Studio

class StudioCreate(CreateView):
  model = Studio
  fields = '__all__'

class StudioUpdate(UpdateView):
  model = Studio
  fields = ['name', 'location']

class StudioDelete(DeleteView):
  model = Studio
  success_url = '/studios/'