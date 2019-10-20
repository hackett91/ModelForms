# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    #order by like sql
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
