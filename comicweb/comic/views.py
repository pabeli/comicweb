from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests 
import json

def index(request):
    
    #Getting the response
    user_agent = request.META["HTTP_USER_AGENT"] # Unique user agent
    r = requests.get('http://comicvine.gamespot.com/api/issues/?api_key=408a81d41cecfbbe5385a6afc633f1c7117c2326&format=json', 
                      headers = { "user-agent": user_agent})
    r_to_json = r.json()
    
    #Getting the info from the response
    results = r_to_json["results"]
    
    context = {
        "results": results,
    }

    #Getting the template for the page
    template = loader.get_template('comic\index.html')

    return HttpResponse(template.render(context, request))

def detail_view(request, detail_id):
    
    api_comic = "https://comicvine.gamespot.com/api/issue/4000-" + str(detail_id) + "/"

    #Getting the json
    url = api_comic + '?api_key=408a81d41cecfbbe5385a6afc633f1c7117c2326&format=json'
    user_agent = request.META["HTTP_USER_AGENT"] # Unique user agent
    r = requests.get(url, headers = { "user-agent": user_agent})
    r_to_json = r.json()
    
    #Getting the info from the json
    results = r_to_json["results"]

    #Image
    image = results["image"]

    #Character credits
    names = []
    for element in results["character_credits"]:
        names.append(str(element["name"]))
    
    #Team credits
    team = []
    for element in results["team_credits"]:
        team.append(str(element["name"]))

    #Location credits
    location = []
    for element in results["location_credits"]:
        location.append(str(element["name"]))

    #Creating the context
    context = {
        "results": results,
        "names": names,
        "team": team,
        "location": location,
        "image": image
    }

    #Getting the template for the page
    template = loader.get_template('comic\detail.html')

    #return HttpResponse(url)
    return HttpResponse(template.render(context, request))



