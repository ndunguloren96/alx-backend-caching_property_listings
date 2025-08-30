from django.http import JsonResponse
from django.views.decorators.cache import cache_page # Correct import
from .models import Property

@cache_page(60 * 15) # Correct decorator
def property_list(request):
    """
    View to list all properties, returning JSON data and
    cached at the view level for 15 minutes.
    """
    properties = Property.objects.all()
    
    # We now convert the queryset objects to a list of dictionaries to make them JSON-serializable.
    data = [{
        'title': p.title,
        'description': p.description,
        'price': str(p.price),
        'location': p.location,
        'created_at': p.created_at.isoformat(),
    } for p in properties]
    
    return JsonResponse({'data': data}, safe=False)
