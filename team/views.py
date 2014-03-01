# Create your views here.
from django.shortcuts import render

def home(request):
    context = {'message': 'Here is a message!'}
    return render(request, "base.html", context)
