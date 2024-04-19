import streamlit as st
from streamlit_dimensions import st_dimensions
import charts as ch
from dataframes import get_clean_dataframe
import config


def main():
    st.set_page_config(
        page_title="Accidents de vélo en France - Histogrammes",
        page_icon="🇫🇷",
        layout="wide",
        )

    st.title("Analyse des accidents de vélo en France")
    st.info(body="Graphiques de type histogramme", icon="📊")
    config.init()
    config.screen_size = st_dimensions(key='main')
    config.screen_size = config.screen_size['width'] if config.screen_size != None else 0

    accidents_velo_df = get_clean_dataframe()
    
    ch.bar_chart_accidents_selon_sexe_par_an(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_an(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_luminosite_par_gravite(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_atmosphere(accidents_velo_df)
    st.divider()
    ch.bar_chart_accidents_selon_gravite_par_tranche_age(accidents_velo_df)


if __name__ == "__main__":
    main()
