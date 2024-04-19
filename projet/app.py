import pandas as pd
import streamlit as st
from streamlit_dimensions import st_dimensions
import charts as ch
from dataframes import get_clean_dataframe, get_dataframe_with_valid_coord
from map import map_container
import config


def app_body(accidents_velo_df: pd.DataFrame):
    with st.sidebar:
        st.page_link("app.py", label="Home", icon="🏠")
    
    map_container(get_dataframe_with_valid_coord(accidents_velo_df))
    st.divider()
    ch.bar_chart_accidents_selon_sexe_par_an(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_an(accidents_velo_df)
    st.divider()
    ch.multiple_line_chart_accidents_selon_gravite_par_an(accidents_velo_df)
    st.divider()
    ch.line_chart_accidents_par_an(accidents_velo_df)
    st.divider()
    ch.pie_chart_accidents_total_container(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_luminosite_par_gravite(accidents_velo_df)
    st.divider()
    ch.line_chart_accidents_selon_heure(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_atmosphere(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_tranche_age(accidents_velo_df)
    st.divider()
    ch.pie_chart_accidents_selon_collision(accidents_velo_df)
    st.divider()
    ch.pie_chart_accidents_selon_tranche_age(accidents_velo_df)


def main():
    st.set_page_config(
        page_title="Accidents de vélo en France",
        page_icon="🇫🇷",
        layout="wide",
        )
    
    st.title("Analyse des accidents de vélo en France")
    st.info(body="Et oui, y'a pas mal d'accidents mine de rien", icon="🔥")
    config.init()
    config.screen_size = st_dimensions(key='main')
    config.screen_size = config.screen_size['width'] if config.screen_size != None else 0

    accidents_velo_df = get_clean_dataframe()

    app_body(accidents_velo_df)


if __name__ == "__main__":
    main()
