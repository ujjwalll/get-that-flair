# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, HttpResponse, render_to_response
from django.conf import settings
from . import Detection as D
import sys
import pandas as pd
# Create your views here.

def index(request):
    
    if request.method == 'POST':
        
        model = settings.MODEL_FILE
        val = request.POST.get('url')
        return render(request,"app/index.html",{"output":D.detect_flair(val,model)[0]})

    return render(request,"app/index.html")

def statistics(request):
      return render_to_response('app/home-2.html')

sys.stdout.flush()



