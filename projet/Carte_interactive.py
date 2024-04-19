import pandas as pd
import streamlit as st
from streamlit_dimensions import st_dimensions
import charts as ch
from dataframes import get_clean_dataframe, get_dataframe_with_valid_coord
from map import map_container
import config


def main():
    st.set_page_config(
        page_title="Accidents de vélo en France - Carte",
        page_icon="🇫🇷",
        layout="wide",
        )

    st.title("Analyse des accidents de vélo en France")
    st.info(body="Carte interactive en fonction des années", icon='🗺️')
    config.init()
    config.screen_size = st_dimensions(key='main')
    config.screen_size = config.screen_size['width'] if config.screen_size != None else 0

    accidents_velo_df = get_clean_dataframe()

    map_container(get_dataframe_with_valid_coord(accidents_velo_df))


if __name__ == "__main__":
    main()
