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
print(user_name) #TODO


# Bouton (boolean)
if st.button("Valider"):
  st.write(f"Bonjour {user_name} !")

# Image
st.image("https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp")

# Video
st.video("https://youtu.be/sgnrL7yo1TE")

# Slider


# Lecture d'un fichier CSV avec pandas

