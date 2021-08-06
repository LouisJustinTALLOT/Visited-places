from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_visited_places/', views.all_visited_places, name='all_visited_places'),
]