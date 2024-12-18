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
    
    prompt1 = st.text_area("Entrez l'url de l'image 1 :")
    prompt2 = st.text_area("Entrez l'url de l'image 2 :")
        
    if st.button("Lancer l'analyse") and prompt:
        response = get_images_comparaison(client, prompt1, prompt2)
        st.write(response)
