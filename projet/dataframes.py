import streamlit as st
import pandas as pd
from pathlib import Path


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


@st.cache_data()
def get_accidents_selon_sexe_an(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['an', 'sexe']][accidents_velo_df['sexe'] != '-1']


@st.cache_data()
def get_accidents_selon_gravite_an_hommes(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['an', 'grav']][accidents_velo_df['sexe'] == 'Masculin']


@st.cache_data()
def get_accidents_selon_gravite_an_femmes(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['an', 'grav']][accidents_velo_df['sexe'] == 'Feminin']


@st.cache_data()
def get_accidents_selon_gravite_an(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['an', 'grav']]


@st.cache_data()
def get_accidents_selon_gravite_luminosite(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['grav', 'lum']]


@st.cache_data()
def get_accidents_par_heure(accidents_velo_df: pd.DataFrame):
    accidents_velo_df['hrmn'] = accidents_velo_df['hrmn'].str[:2].astype(int)
    return accidents_velo_df[['hrmn', 'date']]


@st.cache_data()
def get_accidents_selon_gravite_par_atmosphere(accidents_velo_df: pd.DataFrame):
    return accidents_velo_df[['atm', 'grav']][accidents_velo_df['atm'] != 'Autre'].dropna(subset=['atm'])


@st.cache_data()
def get_accidents_selon_collision(accidents_velo_df: pd.DataFrame):
    accidents_colission_df = accidents_velo_df[['col']].copy()
    return accidents_colission_df[accidents_colission_df['col'] != '-1.0'].dropna(subset='col')


def get_tranche_age_bins_labels():
    bins = [x for x in range(1, 92, 10)]
    bins.append(120)
    labels = [f"{x}-{x+9}" for x in bins][:-2]
    labels.append('91+')
    return bins, labels


@st.cache_data()
def get_accidents_selon_gravite_par_tranche_age(accidents_velo_df: pd.DataFrame):
    bins, labels = get_tranche_age_bins_labels()
    accidents_selon_tranche_age_par_grav = accidents_velo_df[['age', 'grav']].copy()
    accidents_selon_tranche_age_par_grav['tranche_age'] = pd.cut(accidents_selon_tranche_age_par_grav['age'], bins=bins, labels=labels, right=False)
    accidents_selon_tranche_age_par_grav.dropna(subset='tranche_age', inplace=True)
    return accidents_selon_tranche_age_par_grav[['tranche_age', 'grav']]


@st.cache_data()
def get_accidents_selon_tranche_age(accidents_velo_df: pd.DataFrame):
    bins, labels = get_tranche_age_bins_labels()
    accidents_selon_tranche_age = accidents_velo_df[['age']].copy()
    accidents_selon_tranche_age['tranche_age'] = pd.cut(accidents_selon_tranche_age['age'], bins=bins, labels=labels, right=False)
    return accidents_selon_tranche_age[['tranche_age']].dropna()
