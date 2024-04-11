import folium
import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster, BeautifyIcon

@st.cache_data
def get_clean_dataframe():
    csv_path = Path("accidentsVelo.csv")
    accidents_velo_df = pd.read_csv(csv_path)

    accidents_velo_df = accidents_velo_df.rename(columns={'long':'lon'})
    accidents_velo_df = convert_df_lat_lon_column_to_float(accidents_velo_df)

    accidents_velo_df = accidents_velo_df[(accidents_velo_df['lat'].notna()) & (accidents_velo_df['lon'].notna())]
    accidents_velo_df = accidents_velo_df[(accidents_velo_df['lon'] != 0.0) & (accidents_velo_df['lat'] != 0.0)]
    return accidents_velo_df


def convert_to_float(value):
    # Check if value is string and replace ',' with '.'
    if isinstance(value, str):
        return float(value.replace(',', '.'))
    else:
        return float(value)


def convert_df_lat_lon_column_to_float(df: pd.DataFrame) -> pd.DataFrame:
    df['lat'] = df['lat'].apply(convert_to_float)
    df['lon'] = df['lon'].apply(convert_to_float)
    return df


@st.cache_data()
def generate_accidents_map(years, df: pd.DataFrame):
    accidents_map = folium.Map(location=(46.71109, 1.7191036),
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
    

def main():
    st.set_page_config(
    page_title="Accidents de vélo en France",
    page_icon="🇫🇷",
    layout="wide",
    )
    
    st.title("Analyse des accidents de vélo en France")
    st.info(body="Et oui, y'a pas mal d'accidents mine de rien", icon="🔥")

    accidents_velo_df = get_clean_dataframe()

    left, right = st.columns(2)
    
    with left:
        st.header("Carte des accidents en France")
        years = st.multiselect(label='Choisissez une année ou plusieurs années', options=[i for i in range(2005,2022)])

    with right:
        accidents_map = generate_accidents_map(years, df=accidents_velo_df)
        folium_static(accidents_map, width=700, height=700)


if __name__ == "__main__":
    main()
    