# Django methods and classes
from django.shortcuts import render
from django.http import HttpResponse

# Modules for geographical data manipulation
import folium

# My models
from .models import Place
# the associated methods
from .methods import get_total_number_of_places

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
