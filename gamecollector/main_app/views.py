from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, VoiceActor
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
    voice_actors_game_doesnt_have = VoiceActor.objects.exclude(id__in = game.voice_actors.all().values_list('id'))
    playtime_form = PlaytimeForm()
    return render(request, 'games/detail.html', {
        'game': game, 
        'playtime_form': playtime_form,
        'voice_actors': voice_actors_game_doesnt_have
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

def assoc_voice_actor(request, game_id, voice_actor_id):
  # Note that you can pass a toy's id instead of the whole object
  Game.objects.get(id=game_id).voice_actors.add(voice_actor_id)
  return redirect('detail', game_id=game_id)

class VoiceActorList(ListView):
  model = VoiceActor

class VoiceActorDetail(DetailView):
  model = VoiceActor

class VoiceActorCreate(CreateView):
  model = VoiceActor
  fields = '__all__'

class VoiceActorUpdate(UpdateView):
  model = VoiceActor
  fields = ['name', 'age']

class VoiceActorDelete(DeleteView):
  model = VoiceActor
  success_url = '/voice_actors/'