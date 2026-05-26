# 1/ on choisit le fichier xyz du dossier google drive 
#2/ conda activate ESTP26 et streamlit run TP2_évaluation_BIGDATA_Hiba_DRIOWYA.py
#3/on charge les librairies streamlit, numpy, pandas, matplotlib.pyplot et time
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
#4/ on demande à l'utilisateur d'entrer son nom et on le salue 

st.title("TP2_créer une applicationStreamlit")
nom=st.sidebar.text_input("Entrez votre nom:")
if nom:
    st.sidebar.success(f"Bonjour, {nom}!")
#5/Chargement de nos données
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
if uploaded_file is not None:
    st.write("Fichier chargé avec succès!")
    df = pd.read_csv(uploaded_file) #lecture du fichier csv par pandas
    st.dataframe(df.head()) #affichage du dataframe dans streamlit

#6/Utilisation de selectbox pour permettre à l'utilisateur de choisir entre 2D et 3D
st.subheader("Type de visualisation")# Choix du type de visualisation
graph_type = st.sidebar.selectbox("type de graphique", ["2D", "3D"])

#7/ recuperation de la liste des colonnes numériques df.select_dtypes
col_numeric = df.select_dtypes(include='number').columns.tolist()
#8/ choix du graph 2D
if graph_type == "2D":
        st.subheader("Graphique 2D")
        col_x = st.selectbox("Axe X", col_numeric, key="x2d")
        col_y = st.selectbox("Axe Y", col_numeric, key="y2d")
        st.line_chart(data=df, x=col_x, y=col_y)
#9/ choix du graph 3D , en important d'abbord la librairie plotly.express et en utilisant la fonction scatter_3d pour créer le graphique 3D

import plotly.express as px

if graph_type == "3D":
        st.subheader("Graphique 3D")
        col_x = st.selectbox("Axe X", col_numeric, key="x3d")
        col_y = st.selectbox("Axe Y", col_numeric, key="y3d")
        col_z = st.selectbox("Axe Z", col_numeric, key="z3d")
        fig = px.scatter_3d(df, x=col_x, y=col_y, z=col_z)
        st.plotly_chart(fig)
                                                        
