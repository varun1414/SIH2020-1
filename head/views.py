from django.shortcuts import render,HttpResponse

from datetime import date,datetime,timedelta
from django.db import connection
import folium
import os
import json
from login import models as models
# Create your views here.
def dispMap(request,airInfo):


    # Create map object
    m = folium.Map(location=[21.1458, 79.0882],zoom_start=5)

    # Global tooltip
    tooltip = 'Click For More Info'

    # Create custom marker icon
    # logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

    # Vega data
    # vis = os.path.join('data', 'vis.json')

    # Geojson Data
    # overlay = os.path.join('data', 'overlay.json')

    # Create markers
    
    
    for i in airInfo:
        tooltip = i['name']
        dgm=models.Dgm.objects.filter(a_id=i['a_id']).values()
        folium.Marker([i['longitude'], i['latitude']],
                popup=folium.Popup(('<h5>id:{did}</h5><br><h5>name:{dname}</h5><br><h5>contact:{dcontact}</h5><br><h5>email:{demail}</h5><br><a href="/" target="_blank"> {name} </a>').format(did=dgm[0]['dgm_id'],dname=dgm[0]['name'],name=i['name'],dcontact=dgm[0]['contact'],demail=dgm[0]['email'])),
                tooltip=tooltip).add_to(m)
    # folium.Marker([42.333600, -71.109500],
    #             popup='<strong>Location Two</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(icon='cloud')).add_to(m),
    # folium.Marker([42.377120, -71.062400],
    #             popup='<strong>Location Three</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='purple')).add_to(m),
    # folium.Marker([42.374150, -71.122410],
    #             popup='<strong>Location Four</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='green', icon='leaf')).add_to(m),
    # folium.Marker([42.375140, -71.032450],
    #             popup='<strong>Location Five</strong>',
    #             tooltip=tooltip).add_to(m),
                # icon=logoIcon)
    # folium.Marker([42.315140, -71.072450],
    #             popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

    # Circle marker
    # folium.CircleMarker(
    #     location=[42.466470, -70.942110],
    #     radius=50,
    #     popup='My Birthplace',
    #     color='#428bca',
    #     fill=True,
    #     fill_color='#428bca'
    # ).add_to(m)

    # Geojson overlay
    # folium.GeoJson(overlay, name='cambridge').add_to(m)

    m.save('./head/templates/head/map.html')
    return render(request,"./head/map.html")