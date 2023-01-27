from django.shortcuts import render
import folium

# Create your views here.
def index(request):
    # Create a map object
    m = folium.Map()
    m = m._r_repr_html_()
    context = {
        
    }
    return render(request, 'index.html') 
