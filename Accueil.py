import streamlit as st

# Application sans doute non fonctionnelle (tests dans le cadre d'une formation)
st.title('Interface Mistral AI')

# Sous-titre
st.subheader('Mistral AI')

# Zones de texte
st.write("Introduction à Mistral AI")


# ====== Sidebar ======
# Zone de saisie de la clé API MISTRAL
user_name = st.text_input("Quel est votre nom ?")
st.sidebar.tex("https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp")


# ====== Zone principale ======



