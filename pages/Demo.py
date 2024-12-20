import streamlit as st

# Application sans doute non fonctionnelle (tests dans le cadre d'une formation)
st.title('Interface Mistral AI')

# Sous-titre
st.subheader('Mistral AI')

# Zones de texte
st.write("Introduction à Mistral AI")


if st.checkbox("Afficher l'aide de mise en forme du contenu"):
  st.write("""
  # Titre
  
  ## Soustitre
  
  **Gras**
  
  `print("Hello World!)`
  """)

# Zone de saisie
user_name = st.text_input("Quel est votre nom ?")
print(user_name) #TODO affichage dans la console

# Slider
user_age = st.slider("Quel est votre âge ?", 18,99,30)  #valeurs min,max,default

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


# ====== Sidebar ======
# Image dans la sidebar
st.sidebar.image("https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp")
