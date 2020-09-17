from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_playtime/', views.add_playtime, name='add_playtime'),
    path('games/<int:game_id>/assoc_voice_actor/<int:voice_actor_id>/', views.assoc_voice_actor, name='assoc_voice_actor'),
    path('voice_actors/', views.VoiceActorList.as_view(), name='voice_actors_index'),
    path('voice_actors/<int:pk>/', views.VoiceActorDetail.as_view(), name='voice_actors_detail'),
    path('voice_actors/create/', views.VoiceActorCreate.as_view(), name='voice_actors_create'),
    path('voice_actors/<int:pk>/update/', views.VoiceActorUpdate.as_view(), name='voice_actors_update'),
    path('voice_actors/<int:pk>/delete/', views.VoiceActorDelete.as_view(), name='voice_actors_delete'),
]
