# Projet Data Analyse - Accidents de vélo en France

- [Projet Data Analyse - Accidents de vélo en France](#projet-data-analyse---accidents-de-vélo-en-france)
  - [A propos](#a-propos)
    - [Quésaco ?](#quésaco-)
    - [Technologies](#technologies)
    - [Lien du jeu de données](#lien-du-jeu-de-données)
    - [L'équipe](#léquipe)
  - [CSV et Excel](#csv-et-excel)
    - [Modification colonnes :](#modification-colonnes-)
    - [Suppression colonnes :](#suppression-colonnes-)
  - [Installation](#installation)
  - [Utilisation](#utilisation)

## A propos

### Quésaco ?

Une application web servant de tableau de bord avec des graphiques ainsi qu'une carte interactive utilisant les données, nettoyées et analysées, des accidents de vélo en France entre 2005 et 2021.

### Technologies

- Application Web - Dashboard :
  - [Python](https://www.python.org/) (langage de programmation)
  - [Streamlit](https://streamlit.io/) (framework Python pour faire des applications web d'analyse de données)
  - [Pandas](https://pandas.pydata.org/) (librairie Python pour la manipulation et l'analyse de données)
  - [Folium](https://python-visualization.github.io/folium/latest/) (librairie Python pour réaliser des cartes Leaflet avec des données Python)
  - [Altair](https://altair-viz.github.io/) (librairie Python pour la visualisation de données)

- Analyse de données :
  - Excel (logiciel de tableur permettant d'effectuer des calculs (et plein d'autres choses...))
  - [Pandas](https://pandas.pydata.org/)
  - [Jupyter Notebook](https://jupyter.org/)

### Lien du jeu de données

[Dataset des accidents de vélo](https://www.data.gouv.fr/fr/datasets/accidents-de-velo/)

### L'équipe
- Axel BROQUAIRE
- Ethan BENOIT-LISETTE
- Hugo ANDRIAMAMPIANINA
- Joris PELLIER

## CSV et Excel

Pour le CSV nous avons clean avec le fichier [Fichier pour nettoyer accidentsVelo.csv](code_clean.ipynb).  
Ainsi, nous avons modifié certaines colonnes.

### Modification colonnes :

| Colonne | Modification apportée |
|--|--|
| Num_Acc | Suppression des données de test du CSV où "Num_Acc" est égal à 36. |
| Date | Modification des "-" par des "/" pour une lisibilité plus simple. |
| Mois | Remplacement des caractères "é" par "e" et "û" par "u" pour éviter les caractères spéciaux sur les mois (février et août). |
| Lat et Long | Modification des "," par des "." pour faciliter l'utilisation des coordonnées. |
| HrMn | Modification des heures pour qu'elles correspondent au format hh:mm entre 00h00 et 23h59, ajout de "00" après une heure comme "10:", décalage des ":" pour faire passer "91:2" à "9:12", etc. |
| Agg | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Age | Modification du type de la colonne de float à int. |
| Col | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Lum | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Atm | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Grav | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Sexe | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Trajet | Modification des ID par leurs valeurs (voir fichier pour cela). |
| Obs | Modification du type de la colonne de float à int. |
| Obsm | Modification du type de la colonne de float à int. |
| Manv | Modification du type de la colonne de float à int. |
| NumVehicules | Modification du type de la colonne de float à int. |


### Suppression colonnes :

| Colonne | Justification |
|--|--|
| Int |  pas retrouver la valeur des ids. |
| Catr | pas retrouver la valeur des ids. |
| Circ | pas retrouver la valeur des ids. |
| Nbv | pas retrouver la valeur des ids. |
| Prof | pas retrouver la valeur des ids. |
| Plan | pas retrouver la valeur des ids. |
| Surf| pas retrouver la valeur des ids. |
| Infra |  pas retrouver la valeur des ids. |
| Situ |  pas retrouver la valeur des ids. |
| Equipement |  pas retrouver la valeur des ids. |
| Choc |  pas retrouver la valeur des ids. |
| Vehiculeid |  pas d'utilité. |
| TypeVehicules |  pas retrouver la valeur des ids. |
| ManoeuVehicules | pas d'utilité. |

## Installation

- Créer un environnement virtuel Python
```bash
python -m venv .env
```

- Activer l'environnement virtuel
```bash
# Windows
.\.env\Scripts\activate

# Linux
source .env/bin/activate
```

- Installer les packages Python requis à partir du fichier `requirements.txt`
```bash
pip install -r requirements.txt
```

## Utilisation

- Lancer l'application pour accéder au tableau de bord via l'interface de commandes de Streamlit
```bash
cd projet
streamlit run app.py
```

`Nota Bene` : Au lancement, ouvre un nouvel onglet dans votre natigateur