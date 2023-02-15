from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    # Enable search functionality for location via geocoder 
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address input is invalid!')
    # Create a map object
    m = folium.Map(location=[lat, lng], zoom_start=14)
    # When you click popup, you should see a navigation bar of the map
    # folium.Marker([-26.259899, 28.316099], tooltip='Carnival Mall, Brakpan', popup='<a href="#">See mall</a>').add_to(m)
    folium.Marker([lat, lng], tooltip='Click for more', popup=address).add_to(m)
    # Get HTML representation of map object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html',  context) 

def error_404(request, exception):
    return render(request, '404.html')

    