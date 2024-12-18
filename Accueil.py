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


mistral_api_key = None
if len(mistral_api_key) > 1:
  st.write("Introduction à Mistral AI")
  st.sidebar.text_input("Entrez votre clé API", disabled=True)
else:
  mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Générez une clé sur le site https://mistral.ai/")

# Zones de texte




# Bouton (boolean)
if st.button("Valider"):
  st.write(f"Bonjour {user_name}, tu es né en {2024-user_age} !")

user_country = st.selectbox("Sélectionnez votre Pays", ["France", "Espagne", "Italie"])

                         
# Video
st.video("https://youtu.be/sgnrL7yo1TE")



# Lecture d'un fichier CSV avec pandas
import pandas as pd
path_url = "https://raw.githubusercontent.com/Quera-fr/My-Credit/refs/heads/main/Analyse%20des%20donn%C3%A9es/test.csv"
df = pd.read_csv(path_url, delimiter=";")

#st.write(df)
edited_df = st.data_editor(df)

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
edited_csv = convert_df(df)

# Bouton de téléchargement des données CSV
st.download_button(
    label="Download data as CSV",
    data=edited_csv,
    file_name="data_edited.csv",
    mime="text/csv",
)


