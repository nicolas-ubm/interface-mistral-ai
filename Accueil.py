import streamlit as st

# Application sans doute non fonctionnelle (tests dans le cadre d'une formation)
st.title('Interface Mistral AI')

# Sous-titre
st.subheader('Mistral AI')

# Zones de texte
st.write("Introduction à Mistral AI")

st.write("""
# Titre

## Soustitre

**Gras**

`print("Hello World!)`
""")

# Zone de saisie
user_name = st.text_input("Quel est votre nom ?")
st.write("Bonjour {user_name} !")
print(user_name)

# Bouton


# Slider


# Lecture d'un fichier CSV avec pandas

