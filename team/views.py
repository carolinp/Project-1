# Create your views here.
from django.shortcuts import render
from team.models import Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {'message': 'Here is a message!'}
    return render(request, "team/home.html", context)

def roster(request):
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 100)
    page = request.GET.get('page')
    try:
        players=paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(1)
    return render(request, "team/roster.html", {'roster': roster})

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "team/player.html", {'player': player})
