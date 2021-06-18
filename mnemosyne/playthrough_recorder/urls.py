from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage')
    , path('home', views.home, name='homepage')
    , path('new-playthrough/', views.new_playthrough, name='new_playthrough')
    , path('new-game/', views.new_game, name='new_game')
    , path('new-player/', views.new_player, name='new_player')
]