import streamlit as st
from functions import *
from mistralai import Mistral

st.title("Comparaison d'images")

# Demande une clé API
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Vous pouvez générer une clé sur le site https://mistral.ai/")

if not mistral_api_key:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")
else:
    client = Mistral(api_key=mistral_api_key)
    
    image_1_url = st.text_area("Entrez l'url de l'image 1 :")
    image_2_url = st.text_area("Entrez l'url de l'image 2 :")
        
    if st.button("Lancer l'analyse") and image_1_url and image_2_url:
        response = get_images_comparaison(client, image_1_url, image_2_url)
        st.write(response)
