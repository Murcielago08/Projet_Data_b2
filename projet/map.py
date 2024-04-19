import pandas as pd
import streamlit as st
import folium
from folium.plugins import MarkerCluster, BeautifyIcon
from streamlit_folium import folium_static
from streamlit_dimensions import st_dimensions
from math import isnan
import config


def generate_accidents_map(years, df: pd.DataFrame):
    accidents_map = folium.Map(
        location=(46.71109, 1.7191036),
        prefer_canvas=True,
        max_bounds=True,
        zoom_start=6,
        min_zoom=6,
        min_lat=41,
        max_lat=51.5,
        min_lon=-5,
        max_lon=10,
        # tiles='CartoDB dark_matter', # * Dark map
        tiles="cartodb positron" # * Basic white map
        )

    marker_cluster = MarkerCluster().add_to(accidents_map)

    # * Map with filter by years
    for i in df[df['an'].isin(years)].index:
        popup = folium.Popup(f"Date: {df['date'][i]}\nHeure: {df['hrmn'][i]}\nAge: {int(df['age'][i])} ans\nSexe: {"Homme" if df['sexe'][i] == "Masculin" else "Femme"}")
        icon = BeautifyIcon(icon_shape='circle', border_color='red', background_color='red', icon='bicycle', text_color='white')
        folium.Marker(location=[df['lat'][i], df['lon'][i]], icon=icon , popup=popup).add_to(marker_cluster)

    return accidents_map


def map_data_expander(years, accidents_velo_df: pd.DataFrame):
    with st.expander("Voir plus d'informations"):
        average_victim_age = accidents_velo_df[accidents_velo_df['an'].isin(years)]['age'].mean()
        # TODO Ajouter plus d'informations
        st.write(f"""
                 Nombre d'accidents survenus dans les années sélectionnées (dont les coordonnées sont connues) : {len(accidents_velo_df[accidents_velo_df['an'].isin(years)].index)}\n
                 Moyenne d'âge des victimes : {0 if isnan(average_victim_age) else int(average_victim_age)}
                 """)


def map_container(accidents_velo_df: pd.DataFrame):
    st.header("Carte des accidents en France")
    st.text("")
    if config.screen_size > 1220:
        left, right = st.columns(2)
        with left:
            years = st.multiselect(
                label='Choisissez une année ou plusieurs années',
                label_visibility='collapsed',
                options=[i for i in range(2005,2022)],
                placeholder='Choisissez une année ou plusieurs années'
                )

            column_size = st_dimensions(key='column')
            column_size = column_size['width'] if column_size != None else 0
            accidents_map = generate_accidents_map(years, df=accidents_velo_df)
            folium_static(accidents_map, width=column_size, height=700)
        with right:
            map_data_expander(years, accidents_velo_df)
    else:
        years = st.multiselect(
            label='Choisissez une année ou plusieurs années',
            label_visibility='collapsed',
            options=[i for i in range(2005,2022)],
            placeholder='Choisissez une année ou plusieurs années'
            )
        accidents_map = generate_accidents_map(years, df=accidents_velo_df)
        folium_static(accidents_map, width=config.screen_size, height=700)
        map_data_expander(years, accidents_velo_df)