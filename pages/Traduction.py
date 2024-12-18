import streamlit as st


st.title('Traduction')


import os
import streamlit as st

# Obtenir le chemin du répertoire courant
current_directory = os.getcwd()

# Lister tous les fichiers dans le répertoire courant
files = os.listdir(current_directory)

# Afficher la liste des fichiers
st.write("Fichiers dans le dossier courant :")
for file in files:
    st.write(file)
