from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Images

# Create your views here.
def index(request):

    # Getting images
    img = 

    title = 'Home'
    

    return render (request, 'index.html', {"title": title})