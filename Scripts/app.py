"""
Script de création d'une interface utilisateur web avec la lib Steamlit.


Objectif : 
Développer une interface web intéractive pour inférer sur l'api de scoring et illustrer les résultats obtenus.

Workflow de l'application web :

1- charger un fichier csv contenant des données clients,
2- sélectionner un ou plusieurs clients, 
3- envoyer les données à l'API de scoring de crédit, 
4- recevoir en retour et afficher les résultats de la prédiction sous plusieurs formats (valeur prédite, probabilité, explainabilité).
5- afficher les résultats dans l'interface web avec différentes visualisations.

on utilisera la lib streamlit pour créer l'interface web et on la développera en python

"""

# ///////////////////////////////////
# 1- Configuration du script
# ///////////////////////////////////


# import des bibliothèques nécessaires
import streamlit as st
import requests
import pandas as pd
import numpy as np
from loguru import logger

# définition des logger
logger.add("logs/app.log", format="{time} {level} {message}", level="INFO")
logger.add("logs/app_error.log", format="{time} {level} {message}", level="ERROR")
logger.add("logs/app_debug.log", format="{time} {level} {message}", level="DEBUG")


# ///////////////////////////////////
# 2- Définition de l'interface web
# ///////////////////////////////////


# titre de l'application
st.title("Scoring de crédit")
logger.info("Application started")

# chargement du fichier csv contenant les données réelles

uploaded_file = st.file_uploader("upload your data csv file", type="csv")
logger.info("File uploaded")
logger.debug(f"Uploaded file: {uploaded_file}")

if uploaded_file:
    df_data = pd.read_csv(uploaded_file)
    st.write("Preview of your data:")
    st.dataframe(df_data.head())

# sélection de un ou plusieurs clients

# filtre sur le dataframe
st.subheader("Select clients to predict")
selected_indices = st.multiselect(
    "Choose row numbers (indices) to predict",
    df_data.index.tolist()
)

# formatage des données en format json pour l'api
if selected_indices:
    df_selected = df_data.loc[selected_indices]
    df_processed = df_selected.replace({np.nan: None, np.inf: None, -np.inf: None})
    st.write("Selected clients:")
    st.dataframe(df_processed)


# 5- envoyer une requête https pour interroger l'api et renvoyer la prédiction

if st.button("Get Predictions"):
    data_json = df_processed.to_dict(orient="records")
    url = "http://127.0.0.1:8000/predict"  # localhost
    url_cloud = "https://client-scoring-model.onrender.com/predict"
    response = requests.post(url_cloud, 
                             headers={"Content-Type": "application/json"}, 
                             json=data_json)
    
    if response.status_code == 200:
        result = response.json()
        st.subheader("Predictions")
        st.write(result["prediction"])
        st.subheader("Probabilities")
        st.write(result["probabilite_1"])
        st.subheader("Top 5 features by SHAP")
        st.write(result["top_features"])
    else:
        st.error(f"Error: {response.status_code}")


""" 
```bash
python -m streamlit run app.py
```
"""


