from .models import Place

def get_total_number_of_places():
    return Place.objects.count()