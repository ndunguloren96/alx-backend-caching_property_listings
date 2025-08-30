from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties # Add this import for Task 2

def property_list(request):
    """
    View to list all properties, returning JSON data.
    """
    properties = get_all_properties()
    
    # We now convert the queryset objects to a list of dictionaries to make them JSON-serializable.
    data = [{
        'title': p.title,
        'description': p.description,
        'price': str(p.price), # DecimalField needs to be converted to a string
        'location': p.location,
        'created_at': p.created_at.isoformat(), # datetime object needs to be converted
    } for p in properties]
    
    return JsonResponse({'data': data}, safe=False)
