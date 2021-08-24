import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image
import pydeck as pdk
from urllib.error import URLError
import altair as alt
from collections import Counter 

 #mapdata
map_df_olive = pd.read_csv('3dmap_data/olive_3dmap.csv')
# map_df3 = pd.read_csv('3dmap_data/target_olive.csv')
map_df_shrev = pd.read_csv('3dmap_data/shreveport_3dmap.csv')
map_df_grove= pd.read_csv('3dmap_data/groveport_3dmap.csv')

# def hex_to_rgb(h):
#     h = h.lstrip('#')
#     return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# map_df3['color'] = map_df3['color'].apply(hex_to_rgb)

# view_state = pdk.ViewState(
#     latitude=35.1175,
#     longitude=-89.971107,
#     zoom=10
# )

# layer = pdk.Layer(
#     type='PathLayer',
#     data=map_df3,
#     pickable=True,
#     get_color='color',
#     width_scale=20,
#     width_min_pixels=2,
#     get_path='path',
#     get_width=5
# )

# r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={'text': '{name}'})

# st.pydeck_chart(r)


st.header("Map")
st.write("In progress...")
# st.write(map_df)
    
coordinates = pd.DataFrame({
        'lat':[36.240895,36.152476],
        'lon':[-86.756770,-86.857713],
        'name':['Split at Nashville','Merge at Nashville']
    })

@st.cache
def from_data_file(filename):
    url = (
            "https://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename)
    return pd.read_json(url)
# st.dataframe(map_df2)
layer2 =  pdk.Layer(
                "HexagonLayer",
                data=map_df_olive,
                get_position=["lon", "lat"],
                radius=4600,
                elevation_scale=150,
                elevation_range=[0, 500],
                extruded=True,
            ),

# layer3= pdk.Layer(
#                 "PathLayer",
#                 data=map_df3,
#                 pickable=True,
#                 get_color='color',
#                 width_scale=20,
#                 width_min_pixels=2,
#                 get_path='path',
#                 get_width=5
#             ),
st.header('Olive lane') 
st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={"latitude": 36.174465,
                                        "longitude": -86.767960, "zoom": 11, "pitch": 50},           
                    layers=[layer2],
                    tooltip={
        'html': '<b>Name:</b> {name}',
        'style': {
            'color': 'black'
        }
    },       
                ))
st.header('Shreveport')     
layer3 =  pdk.Layer(
                "HexagonLayer",
                data=map_df_shrev,
                get_position=["lon", "lat"],
                radius=4600,
                elevation_scale=150,
                elevation_range=[0, 500],
                extruded=True,
            ),
st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={"latitude": 36.174465,
                                        "longitude": -86.767960, "zoom": 11, "pitch": 50},           
                    layers=[layer3],
                    tooltip={
        'html': '<b>Name:</b> {name}',
        'style': {
            'color': 'black'
        }
    },       
                ))

st.header('Groveport')             
layer4 =  pdk.Layer(
                "HexagonLayer",
                data=map_df_grove,
                get_position=["lon", "lat"],
                radius=3000,
                elevation_scale=200,
                elevation_range=[0, 200],
                extruded=True,
            ),
st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={"latitude": 36.174465,
                                        "longitude": -86.767960, "zoom": 11, "pitch": 50},           
                    layers=[layer4],
                    tooltip={
        'html': '<b>Name:</b> {name}',
        'style': {
            'color': 'black'
        }
    },       
                ))




# midpoint = (np.average(combine_df["origin_lat"]), np.average(combine_df["origin_long"]))
# st.write(pdk.Deck(
#         map_style ="mapbox://styles / mapbox / light-v9",
#         initial_view_state ={
#             "latitude": midpoint[0],
#             "longitude": midpoint[1],
#             "zoom": 11,
#             "pitch": 50,
#         },
#         layers =[
#             pdk.Layer(
#             "HexagonLayer",
#             data = combine_df[['travel_time', 'origin_lat', 'origin_long']],
#             get_position =["longitude", "latitude"],
#             auto_highlight = True,
#             radius = 100,
#             extruded = True,
#             pickable = True,
#             elevation_scale = 4,
#             elevation_range =[0, 1000],
#             ),
#         ],
#     ))

# @st.cache
# def from_data_file(filename):
#         url = (
#             "https://raw.githubusercontent.com/streamlit/"
#             "example-data/master/hello/v1/%s" % filename)
#     return pd.read_json(url)

# try:
#         ALL_LAYERS = {
#             "Bike Rentals": pdk.Layer(
#                 "HexagonLayer",
#                 data=from_data_file("bike_rental_stats.json"),
#                 get_position=["lon", "lat"],
#                 radius=200,
#                 elevation_scale=4,
#                 elevation_range=[0, 1000],
#                 extruded=True,
#             ),
#             "Bart Stop Exits": pdk.Layer(
#                 "ScatterplotLayer",
#                 data=from_data_file("bart_stop_stats.json"),
#                 get_position=["lon", "lat"],
#                 get_color=[200, 30, 0, 160],
#                 get_radius="[exits]",
#                 radius_scale=0.05,
#             ),
#             "Bart Stop Names": pdk.Layer(
#                 "TextLayer",
#                 data=from_data_file("bart_stop_stats.json"),
#                 get_position=["lon", "lat"],
#                 get_text="name",
#                 get_color=[0, 0, 0, 200],
#                 get_size=15,
#                 get_alignment_baseline="'bottom'",
#             ),
#             "Outbound Flow": pdk.Layer(
#                 "ArcLayer",
#                 data=from_data_file("bart_path_stats.json"),
#                 get_source_position=["lon", "lat"],
#                 get_target_position=["lon2", "lat2"],
#                 get_source_color=[200, 30, 0, 160],
#                 get_target_color=[200, 30, 0, 160],
#                 auto_highlight=True,
#                 width_scale=0.0001,
#                 get_width="outbound",
#                 width_min_pixels=3,
#                 width_max_pixels=30,
#             ),
#         }
#     st.sidebar.markdown('### Map Layers')
#     selected_layers = [
#         layer for layer_name, layer in ALL_LAYERS.items()
#         if st.sidebar.checkbox(layer_name, True)]
#     if selected_layers:
#         st.pydeck_chart(pdk.Deck(
#                 map_style="mapbox://styles/mapbox/light-v9",
#                 initial_view_state={"latitude": 37.76,
#                                     "longitude": -122.4, "zoom": 11, "pitch": 50},
#                 layers=selected_layers,
#             ))
#     else:
#         st.error("Please choose at least one layer above.")
# except URLError as e:
#     st.error("""
#             **This demo requires internet access.**

#             Connection error: %s
#         """ % e.reason)