import folium

map_osm = folium.Map(location=[37.511050, 126.977893])
x = 37.511050
y = 127.098178
lotte = folium.Map(location=[x,y], zoom_start=10)
folium.Marker(location=[x,y], popup='롯데월드').add_to(lotte)
folium.CircleMarker(location=[x,y], radius=10, popup='송파구', color='red', fill_color='blue').add_to(lotte)
lotte.save('lotte.html')