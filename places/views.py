# Django methods and classes
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Modules for geographical data manipulation
import folium

# My models
from .models import Place
# the associated methods
from .methods import get_total_number_of_places
# and the associated forms
from .forms import PlaceForm

def index(request):
    return HttpResponse("Hello, world. You're at the places index.")

def all_visited_places(request):
    # create a map
    m = folium.Map(location=[48.844952, 2.339193], zoom_start=4)

    # get all Places objects
    places = Place.objects.all()
    for place in places:
        # add a marker to the map
        long, lat = place.coordinates.coords
        folium.Marker([lat, long], popup=place.name).add_to(m)

    # return the map
    final_map = m._repr_html_()
    
    total_number_of_places = get_total_number_of_places()
    return render(request, 'places/all_visited_places.html', locals())

def new_visited_place(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlaceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/places/new_visited_place/?place_registered=1')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = PlaceForm()

    return render(request, 'places/new_visited_place.html', locals())