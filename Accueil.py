import streamlit as st

# Application sans doute non fonctionnelle (tests dans le cadre d'une formation)
st.title('Interface Mistral AI')
st.set_page_config(page_title="Ex-stream-ly Cool App",    page_icon="🧊",    layout="wide")


# ====== Sidebar ======
# Image dans la sidebar
st.sidebar.image("https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp")

# Demande clé API
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Générez une clé sur le site https://mistral.ai/")

if mistral_api_key:
    st.write("Introduction à Mistral AI")
else:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")
