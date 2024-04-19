import streamlit as st
from streamlit_dimensions import st_dimensions
import charts as ch
from dataframes import get_clean_dataframe
import config


def main():
    st.set_page_config(
        page_title="Accidents de vélo en France - Courbes",
        page_icon="🇫🇷",
        layout="wide",
        )

    st.title("Analyse des accidents de vélo en France")
    st.info(body="Graphiques de type courbe", icon="📈")
    config.init()
    config.screen_size = st_dimensions(key='main')
    config.screen_size = config.screen_size['width'] if config.screen_size != None else 0

    accidents_velo_df = get_clean_dataframe()

    ch.multiple_line_chart_accidents_selon_gravite_par_an(accidents_velo_df)
    st.divider()
    ch.line_chart_accidents_par_an(accidents_velo_df)
    st.divider()
    ch.line_chart_accidents_selon_heure(accidents_velo_df)


if __name__ == "__main__":
    main()
