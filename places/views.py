# Django methods and classes
from django.shortcuts import render
from django.http import HttpResponse

# Modules for geographical data manipulation
import folium

def index(request):
    return HttpResponse("Hello, world. You're at the places index.")

def all_visited_places(request):
    m = folium.Map(location=[48.844952, 2.339193], zoom_start=4)

    final_map = m._repr_html_()

    return render(request, 'places/all_visited_places.html', locals())