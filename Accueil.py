import streamlit as st

# Application sans doute non fonctionnelle (tests dans le cadre d'une formation)
st.title('Interface Mistral AI')

# ====== Sidebar ======
# Demande clé API
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Générez une clé sur le site https://mistral.ai/")

if mistral_api_key:
    st.write("Introduction à Mistral AI")
else:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")
