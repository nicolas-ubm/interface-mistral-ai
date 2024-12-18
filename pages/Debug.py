import os
import streamlit as st

st.title('DEBUG')

st.subheader("Versions")
st.write(f"Version de Streamlit : {_.__version__}")

st.subheader("Fichiers dans le dossier courant")
# Obtenir le chemin du répertoire courant
current_directory = os.getcwd()

# Lister tous les fichiers dans le répertoire courant
files = os.listdir(current_directory)

# Afficher la liste des fichiers
for file in files:
    st.write(file)

