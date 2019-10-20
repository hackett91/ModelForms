# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
# from first_app.models import User
from first_app.forms  import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def users(request):

    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        #save it to the database commit=True persist it Also can do custom validation here
        if form.is_valid():
            form.save(commit=True)
            #return to homepage
            return index(request)
        #can raise an error
        else:
            print('Error Form invalid')
    return render(request, 'first_app/users.html',{'form': form})

