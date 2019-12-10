import logging
from django.shortcuts import render

# Create your views here.

def index(request):
    logging.info('logging ok...')
    return render(request,"index.html")

def list(request,cat,pages=1):
    print('cat:{0},pages={1}'.format(cat,pages))
    return render(request,"list.html")

def detail(request,id):
    return render(request,"detail.html")