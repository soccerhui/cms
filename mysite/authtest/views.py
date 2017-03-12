
from __future__ import  unicode_literals
from django.shortcuts import render

import json

# Create your views here.

def home(request):
    List = ['zzz', 'ajson']
    Dict = {'site':'ziasd', 'author':'ym'}
    return render(request, 'home.html', {
        'List':json.dumps(List),
        'Dict':json.dumps(Dict)
    })
