from .models import Stay

def get_total_number_of_places():
    return Stay.objects.count()