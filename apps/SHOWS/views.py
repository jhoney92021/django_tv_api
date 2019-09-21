from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers #API Calls
import json #MAYBE WILL HELP WITH SINGLE OBJECT
from django.contrib import messages
from .models import *
import random, datetime

def myConverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def stringifyShow(mShow):
    print('*'*50, '\n', mShow, '\n', '*'*50)
    mJson = {
        "title": mShow.title,
        "network": mShow.network,
        "description": mShow.description,
        "release_date": mShow.release_date,
        "created_at": mShow.created_at,
        "updated_at": mShow.updated_at
    }
    print('*'*50, '\n', mJson, '\n', '*'*50)
    return  mJson
    

def index(request): #Redirect
    return redirect('/shows')

def shows(request):
    #get all shows
    shows = Shows.objects.all()    
    data = serializers.serialize('json', shows)
    return HttpResponse(data, content_type='application/json')

def showDetails(request, showID): #Render FOR DETAILS
    thisShow = Shows.objects.get(id= showID)
    print('*'*50, '\n', thisShow, '\n', '*'*50)

    thisShow = stringifyShow(thisShow)
    print('*'*50, '\n', thisShow, '\n', '*'*50)

    data = json.dumps(thisShow, default= myConverter)
    return HttpResponse(data, content_type='application/json')

def newShow(request):
    #make a show
    errors = Shows.objects.validator(request.POST)

    if len(errors) > 0:
        for tags, value in errors.items():
            print('*'*50, '\n', 'processing', '\n', '*'*50)
            data = messages.error(request, value)
        return HttpResponse(data, content_type='application/json')

    else:
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        description = request.POST['description']
        if title != '':
            newShow = Shows.objects.create(title=title, network=network, description=description, release_date=release)
        messages.success(request, "Successfully added")
        data = newShow
        return HttpResponse(data, content_type='application/json')

# def shows(request): 
#     #Render MAIN PAGE
#     context = {
#         'Shows': Shows.objects.all()

#     }
#     return render(request, 'SHOWS/index.html', context)

def newShow(request): 
    #Render FOR NEW SHOW
    context = {

    }
    return render(request, 'SHOWS/newshow.html', context)

def newShowProcess(request): #Process FOR NEW SHOW
    
    errors = Shows.objects.validator(request.POST)

    if len(errors) > 0:
        for tags, value in errors.items():
            print('*'*50, '\n', 'processing', '\n', '*'*50)
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        description = request.POST['description']
        if title != '':
            newShow = Shows.objects.create(title=title, network=network, description=description, release_date=release)
        messages.success(request, "Successfully added")
        return redirect('/shows/details/%s' % (newShow.id))

# def showDetails(request, showID): #Render FOR DETAILS
#     context = {
#         'thisShow': Shows.objects.get(id= showID)

#     }

#     return render(request, 'SHOWS/details.html', context)

def showEdit(request, showID): #Render FOR SHOW EDIT
    context = {
        'thisShow': Shows.objects.get(id= showID)
    }
    return render(request, 'SHOWS/edit.html', context)

def showEditProcess(request, showID): #Process FOR SHOW EDIT

    errors = Shows.objects.validator(request.POST)

    if len(errors) > 0:
        for tags, value in errors.items():
            print('*'*50, '\n', 'processing', '\n', '*'*50)
            messages.error(request, value)
        return redirect('/shows/details/%s/edit' % (showID))
    else:
        thisShow = Shows.objects.get(id= showID)
        thisShow.title = request.POST['title']  or thisShow.title
        thisShow.network = request.POST['network']  or thisShow.network
        thisShow.release_date = request.POST['release']  or thisShow.release_date
        thisShow.description = request.POST['description']  or thisShow.description
        thisShow.save()
        return redirect('/shows/details/%s' % (showID))

def showDelete(request, showID): #Process for Delete
    thisShow = Shows.objects.get(id= showID)
    thisShow.delete()
    return redirect('/shows')
