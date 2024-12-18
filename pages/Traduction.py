import streamlit as st
from functions import *
from mistralai import Mistral


# ====== Sidebar ======
# Demande clé API
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Générez une clé sur le site https://mistral.ai/")

if mistral_api_key:
    st.write("Introduction à Mistral AI")
else:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")

# ====== Contenu ======
st.title('Traduction')

client = Mistral(api_key = mistral_api_key)

prompt = st.text_area("Prompt :")

response = get_ner(client, prompt)
st.write(response)
