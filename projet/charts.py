import altair as alt
import streamlit as st
import dataframes as df
import pandas as pd
import config



def get_years_chart_hover() -> alt.Parameter:
    return alt.selection_point(
        fields=["an"],
        nearest=True,
        on="mouseover",
        empty=False,
    )


def bar_chart_accidents_selon_gravite_par_an(accidents_velo_df: pd.DataFrame):
    st.subheader("Nombre d'accidents de vélo par an en fonction de la gravité pour les hommes de 2005 à 2021")
    st.text("")
    accidents_selon_gravite_par_an_hommes_df = df.get_accidents_selon_gravite_an_hommes(accidents_velo_df)
    bar_chart = alt.Chart(accidents_selon_gravite_par_an_hommes_df).mark_bar().encode(
        x=alt.X('grav', sort = ["Indemne", "Leger", "Hospitalise", "Mort"], axis=None, title=None),
        y=alt.Y('count(grav)', title="Nombre d'accidents"),
        color=alt.Color('grav', scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#73A5C6', '#528AAE', '#2E5984', '#1E3F66']), title="Gravité de l'accident", legend=alt.Legend(orient='top') ),
        column=alt.Column('an', spacing=5, header=alt.Header(labelOrient = "bottom", title=None)),
    ).configure_view(
        stroke='transparent',
    ).properties(
        width=config.screen_size/20,
        height=400,
    )
    st.altair_chart(bar_chart)
    st.divider()
    st.subheader("Nombre d'accidents de vélo par année en fonction de la gravité pour les femmes de 2005 à 2021")
    st.text("")
    accidents_selon_gravite_par_an_femmes_df = df.get_accidents_selon_gravite_an_femmes(accidents_velo_df)
    bar_chart = alt.Chart(accidents_selon_gravite_par_an_femmes_df).mark_bar().encode(
        x=alt.X('grav', sort = ["Indemne", "Leger", "Hospitalise", "Mort"], axis=None, title=None),
        y=alt.Y('count(grav)', title="Nombre d'accidents"),
        color=alt.Color('grav', scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#b000b2', '#93009c', '#6b0078', '#380356']), title="Gravité de l'accident", legend=alt.Legend(orient='top') ),
        column=alt.Column('an', spacing=5, header=alt.Header(labelOrient = "bottom", title=None)),
    ).configure_view(
        stroke='transparent',
    ).properties(
        width=config.screen_size/20,
        height=400,
    )
    st.altair_chart(bar_chart)


def bar_chart_accidents_selon_sexe_par_an(accidents_velo_df: pd.DataFrame):
    st.subheader("Nombre d'accidents de vélo par année en fonction du sexe de la victime de 2005 à 2021")
    accidents_selon_sexe_par_an_df = df.get_accidents_selon_sexe_an(accidents_velo_df)
    bar_chart = alt.Chart(accidents_selon_sexe_par_an_df).mark_bar().encode(
        x=alt.X('sexe', sort=["Masculin", "Feminin"], axis=None, title=None),
        y=alt.Y('count(sexe)', title="Nombre d'accidents"),
        color=alt.Color('sexe', scale=alt.Scale(domain=["Masculin", "Feminin"], range=['#528AAE', '#b000b2']), title="Sexe de la victime", legend=alt.Legend(orient='top') ),
        column=alt.Column('an', spacing=5, header=alt.Header(labelOrient = "bottom", title=None)),
    ).configure_view(
        stroke='transparent',
    ).properties(
        width=config.screen_size/20,
        height=400,
    )
    st.altair_chart(bar_chart)

    
def multiple_line_chart_accidents_selon_gravite_par_an(accidents_velo_df: pd.DataFrame):
    accidents_selon_grav_an = df.get_accidents_selon_gravite_an(accidents_velo_df)
    st.header("Evolution du nombre d'accidents par année en fonction de la gravité")
    
    # Defines a hover event on each point of the chart where the nearest point is selected
    hover = get_years_chart_hover()
    
    multiple_line_chart = alt.Chart(accidents_selon_grav_an).mark_line(strokeWidth=4).encode(
        x=alt.X('an:N', title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y('count(grav)', title="Nombre d'accidents"),
        color=alt.Color('grav', scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#C5FF95', '#5DEBD7', '#1679AB', '#074173']), title="Gravité de l'accident", legend=alt.Legend(orient='top')),
    ).properties(
        width=config.screen_size/1.5 if config.screen_size > 1220 else config.screen_size,
        height=400
    )
    
    # Add points on the line when hovering it for better visualization
    points = multiple_line_chart.transform_filter(hover).mark_circle(size=65)
    
    # Add popup to see the informations of the hovered point
    tooltips = (alt.Chart(accidents_selon_grav_an)
        .mark_rule(color="#F0F2F6")
        .encode(
            x="an:N",
            y="count(grav)",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("an", title="Année"),
                alt.Tooltip("count(grav)", title="Nombre d'accidents"),
                alt.Tooltip("grav", title="Gravité de l'accident"),
            ],
        )
        .add_params(hover)
    )
        
    st.altair_chart((multiple_line_chart + points + tooltips).interactive())


def line_chart_accidents_par_an(accidents_velo_df: pd.DataFrame):
    st.header("Evolution du nombre d'accidents par année")
    
    hover = get_years_chart_hover()
    
    line_chart = alt.Chart(accidents_velo_df).mark_line(strokeWidth=4).encode(
        x=alt.X('an:N', title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y('count(date)', title="Nombre d'accidents"),
    ).properties(
        width=config.screen_size/1.5 if config.screen_size > 1220 else config.screen_size,
        height=400
    )
    
    points = line_chart.transform_filter(hover).mark_circle(size=65)
    
    tooltips = (alt.Chart(accidents_velo_df)
        .mark_rule(color="#F0F2F6")
        .encode(
            x="an:N",
            y="count(date)",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("an", title="Année"),
                alt.Tooltip("count(date)", title="Nombre d'accidents"),
            ],
        )
        .add_params(hover)
    )

    st.altair_chart((line_chart + points + tooltips).interactive())


def pie_chart_accidents_hommes_total(accidents_velo_df: pd.DataFrame):
    pie_chart = alt.Chart(df.get_accidents_selon_gravite_an_hommes(accidents_velo_df)).mark_arc().encode(
        theta=alt.Theta("count(grav)", title="Nombre d'accidents"),
        color=alt.Color("grav", scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#FFFAF0', '#F27F7E', '#FF211F', '#8D0D22']), title="Gravité de l'accident")
    )
    st.altair_chart(pie_chart, use_container_width=True)


def pie_chart_accidents_femmes_total(accidents_velo_df: pd.DataFrame):
    pie_chart = alt.Chart(df.get_accidents_selon_gravite_an_femmes(accidents_velo_df)).mark_arc().encode(
        theta=alt.Theta("count(grav)", title="Nombre d'accidents"),
        color=alt.Color("grav", scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#FFFAF0', '#F27F7E', '#FF211F', '#8D0D22']), title="Gravité de l'accident")
    )
    st.altair_chart(pie_chart, use_container_width=True)


def pie_chart_accidents_total_container(accidents_velo_df: pd.DataFrame):
    st.header("Part des accidents en fonction de la gravité entre 2005 et 2021")
    st.text("")
    left, right = st.columns(2)
    with left:
        st.subheader("Pour les hommes")
        st.text("")
        pie_chart_accidents_hommes_total(accidents_velo_df)
    with right:
        st.subheader("Pour les femmes")
        st.text("")
        pie_chart_accidents_femmes_total(accidents_velo_df)


def bar_chart_accidents_selon_luminosite_par_gravite(accidents_velo_df: pd.DataFrame):
    st.header("Nombre d'accidents en fonction de la luminosité entre 2005 et 2021")
    st.text("")
    accidents_selon_luminosite_par_gravite_df = df.get_accidents_selon_gravite_luminosite(accidents_velo_df)

    bar_chart = alt.Chart(accidents_selon_luminosite_par_gravite_df).mark_bar(size=50).encode(
        x=alt.X('count(lum)', title="Nombre d'accidents"),
        y=alt.Y('grav', title="Gravité de l'accident", axis=alt.Axis(labelAngle=0, title=None)),
        color=alt.Color('lum', title="Luminosité ambiante", legend=alt.Legend(orient='top') ),
    ).configure_view(
        stroke='transparent',
    ).properties(
        height=400
    )

    st.altair_chart(bar_chart, use_container_width=True)


def line_chart_accidents_selon_heure(accidents_velo_df: pd.DataFrame):
    st.header("Nombre total d'accidents en fonction de l'heure entre 2005 et 2021")
    st.text("")
    
    line_chart = alt.Chart(df.get_accidents_par_heure(accidents_velo_df)).mark_line(strokeWidth=4).encode(
        x=alt.X('hrmn:N', title="Heure", axis=alt.Axis(labelAngle=0, title=None)),
        y=alt.Y('count(hrmn)', title="Nombre d'accidents"),
    ).properties(
        width=config.screen_size/1.5 if config.screen_size > 1220 else config.screen_size,
        height=400
    )

    st.altair_chart(line_chart.interactive())


def bar_chart_accidents_selon_gravite_par_atmosphere(accidents_velo_df: pd.DataFrame):
    st.header("Pourcentage du nombre d'accidents en fonction de l'atmosphère et de la gravité")
    
    bar_chart = alt.Chart(df.get_accidents_selon_gravite_par_atmosphere(accidents_velo_df)).mark_bar().encode(
        x=alt.X('atm', axis=alt.Axis(labelAngle=0), title=None),
        y=alt.Y('count(grav):Q', title="Pourcentage d'accidents", stack="normalize", axis=alt.Axis(format='%')),
        color=alt.Color('grav', scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#FFFAF0', '#F27F7E', '#FF211F', '#8D0D22']), title="Gravité de l'accident", legend=alt.Legend(orient='top'))
    ).configure_view(
        stroke='transparent',
    ).properties(
        height=400,
    )
    
    st.altair_chart(bar_chart, use_container_width=True)


def bar_chart_accidents_selon_gravite_par_tranche_age(accidents_velo_df: pd.DataFrame):
    st.header("Pourcentage du nombre d'accidents en fonction de la gravité par tranche d'âge")
    
    bar_chart = alt.Chart(df.get_accidents_selon_gravite_par_tranche_age(accidents_velo_df)).mark_bar().encode(
        x=alt.X('tranche_age', title="Tranche d'âge", axis=alt.Axis(labelAngle=0)),
        y=alt.Y('count(grav):Q', title="Pourcentage d'accidents", stack="normalize", axis=alt.Axis(format='%')),
        color=alt.Color('grav', scale=alt.Scale(domain=["Indemne", "Leger", "Hospitalise", "Mort"], range=['#FFFAF0', '#F27F7E', '#FF211F', '#8D0D22']), title="Gravité de l'accident", legend=alt.Legend(orient='top'))
    ).configure_view(
        stroke='transparent',
    ).properties(
        height=400,
    )
    
    st.altair_chart(bar_chart, use_container_width=True)


def pie_chart_accidents_selon_collision(accidents_velo_df: pd.DataFrame):
    st.header("Part des accidents en fonction de le type de collision")
    pie_chart = alt.Chart(df.get_accidents_selon_collision(accidents_velo_df)).mark_arc().encode(
        theta=alt.Theta("count(col):Q", title="Nombre d'accidents"),
        color=alt.Color("col:N", title="Gravité de l'accident")
    )
    left, _ = st.columns(2)
    with left:
        st.altair_chart(pie_chart, use_container_width=True)


def pie_chart_accidents_selon_tranche_age(accidents_velo_df: pd.DataFrame):
    st.header("Part des accidents en fonction de la tranche d'âge")
    
    accidents_selon_tranche_age_df = df.get_accidents_selon_tranche_age(accidents_velo_df)

    pie_chart = alt.Chart(accidents_selon_tranche_age_df).mark_arc().encode(
        theta=alt.Theta("count(tranche_age):Q", title="Nombre d'accidents"),
        color=alt.Color("tranche_age:N", title="Tranche d'âge"),
    )
    left, _ = st.columns(2)
    with left:
        st.altair_chart(pie_chart, use_container_width=True)