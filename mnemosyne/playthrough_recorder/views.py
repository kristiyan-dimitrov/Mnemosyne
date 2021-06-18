from django.shortcuts import render
from django.db.models import AutoField

# Create your views here.

def home(request):
    """
    The goal of this view is to serve as the homepage for the playthrough tracker.
    It should display the most recent playthroughs

    :param request: request sent by the user's browser to display page
    :return: renders an html template
    """

    # context = {'auto_field': str(AutoField)}

    return render(request, 'playthrough_recorder/home.html')


def new_playthrough(request):
    """
    The goal of this view is to serve as the homepage for the playthrough tracker.
    It should display the most recent playthroughs

    :param request: request sent by the user's browser to display page
    :return: renders an html template
    """
    return render(request, 'playthrough_recorder/new_playthrough.html')


def new_game(request):
    """
    The goal of this view is to serve as the homepage for the playthrough tracker.
    It should display the most recent playthroughs

    :param request: request sent by the user's browser to display page
    :return: renders an html template
    """
    return render(request, 'playthrough_recorder/new_game.html')


def new_player(request):
    """
    The goal of this view is to serve as the homepage for the playthrough tracker.
    It should display the most recent playthroughs

    :param request: request sent by the user's browser to display page
    :return: renders an html template
    """
    return render(request, 'playthrough_recorder/new_player.html')