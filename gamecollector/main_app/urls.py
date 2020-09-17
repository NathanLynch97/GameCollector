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
    path('studios/', views.StudioList.as_view(), name='studios_index'),
    path('studios/<int:pk>/', views.StudioDetail.as_view(), name='studios_detail'),
    path('studios/create/', views.StudioCreate.as_view(), name='studios_create'),
    path('studios/<int:pk>/update/', views.StudioUpdate.as_view(), name='studios_update'),
    path('studios/<int:pk>/delete/', views.StudioDelete.as_view(), name='studios_delete'),
]
