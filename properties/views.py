from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    """
    View to list all properties, returning JSON data and using
    the low-level cache from the get_all_properties utility function.
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
