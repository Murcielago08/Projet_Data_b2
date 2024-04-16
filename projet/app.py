import folium
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster, BeautifyIcon
from math import isnan
from streamlit_dimensions import st_dimensions


@st.cache_data
def get_clean_dataframe():
    csv_path = Path("data_clean.csv")
    accidents_velo_df = pd.read_csv(csv_path, sep=';')
    accidents_velo_df = accidents_velo_df.rename(columns={'long':'lon'})
    return accidents_velo_df


@st.cache_data
def get_dataframe_with_valid_coord(df: pd.DataFrame):
    df = df[(df['lat'].notna()) & (df['lon'].notna())]
    df = df[(df['lon'] != 0.0) & (df['lat'] != 0.0)]
    return df


# @st.cache_data()
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
        popup = folium.Popup(f"Date: {df['date'][i]}\nHeure: {df['hrmn'][i]}\nAge: {df['age'][i]}\nSexe: {"Homme" if df['sexe'][i] == 1 else "Femme"}")
        icon = BeautifyIcon(icon_shape='circle', border_color='red', background_color='red', icon='bicycle', text_color='white')
        folium.Marker(location=[df['lat'][i], df['lon'][i]], icon=icon , popup=popup).add_to(marker_cluster)

    return accidents_map


def map_container(accidents_velo_df: pd.DataFrame):
    st.header("Carte des accidents en France")
    
    if screen_size > 1220:
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
        folium_static(accidents_map, width=screen_size, height=700)
        map_data_expander(years, accidents_velo_df)
        

def map_data_expander(years, accidents_velo_df: pd.DataFrame):
    with st.expander("Voir plus d'informations"):
        average_victim_age = accidents_velo_df[accidents_velo_df['an'].isin(years)]['age'].mean()
        # TODO Ajouter plus d'informations
        st.write(f"""
                 Nombre d'accidents survenus dans les années sélectionnées (dont les coordonnées sont connues) : {len(accidents_velo_df[accidents_velo_df['an'].isin(years)].index)}\n
                 Age moyen des victimes : {0 if isnan(average_victim_age) else int(average_victim_age)}
                 """)


def get_accidents_selon_sexe_par_an(accidents_velo_df: pd.DataFrame):
    accidents_velo_df = accidents_velo_df[['an', 'sexe']][accidents_velo_df['sexe'] != '-1']
    return accidents_velo_df


def main():
    st.set_page_config(
        page_title="Accidents de vélo en France",
        page_icon="🇫🇷",
        layout="wide",
        )
    
    st.title("Analyse des accidents de vélo en France")
    st.info(body="Et oui, y'a pas mal d'accidents mine de rien", icon="🔥")
    global screen_size 
    screen_size = st_dimensions(key='main')
    screen_size = screen_size['width'] if screen_size != None else 0
    accidents_velo_df = get_clean_dataframe()

    map_container(get_dataframe_with_valid_coord(accidents_velo_df))
    
    accidents_selon_sexe_par_an_df = get_accidents_selon_sexe_par_an(accidents_velo_df)
    
    
    
    bar_chart = alt.Chart(accidents_selon_sexe_par_an_df, title="Nombre d'accidents de vélo par an en fonction du sexe de la victime de 2005 à 2021").mark_bar().encode(
        x=alt.X('sexe', sort = ["Masculin", "Feminin"], axis=None),
        y=alt.Y('count(sexe)', title="Nombre d'accidents"),
        color=alt.Color('sexe', scale=alt.Scale(range=['#EA98D2', '#659CCA']), title="Sexe de la victime"),
        column=alt.Column('an', spacing=5, header=alt.Header(labelOrient = "bottom", title=None)),
    ).configure_view(
        stroke='transparent',
    ).properties(
        width=screen_size/24,
        height=300,
    )
    left, _ = st.columns(2)
    with left:
        st.altair_chart(bar_chart)
        # st.bar_chart(accidents_selon_sexe_par_an_df, x='an', y=['Masculin','Feminin'])


if __name__ == "__main__":
    main()
