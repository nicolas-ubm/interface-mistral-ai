import streamlit as st
from functions import *
from mistralai import Mistral

st.title('Traduction')

# Demande une clé API
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Vous pouvez générer une clé sur le site https://mistral.ai/")

# Vérifier si la clé API est renseignée
if not mistral_api_key:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")
else:
    # Initialisation du client
    client = Mistral(api_key=mistral_api_key)
    
    # Champ pour le texte à traduire
    prompt = st.text_area("Entrez le texte à traduire :")
    
    # Sélection de la langue de traduction
    trad_lang = st.selectbox(
        "Sélectionnez la langue",
        ["français", "allemand", "anglais", "espagnol", "japonais"],  # Assurez-vous que les clés correspondent à celles utilisées dans la réponse
        index=2  # Par défaut : "anglais"
    )
    
    # Bouton pour exécuter la traduction
    if st.button("Exécuter") and prompt:
        response = get_translation(client, prompt)
        
        try:
            # Supposons que `response` contient un JSON avec les traductions
            translations = response  # Si nécessaire, utilisez `json.loads(response)` pour convertir en dict
            if trad_lang in translations:
                st.success(f"Traduction ({trad_lang.capitalize()}): {translations[trad_lang]}")
            else:
                st.error("Langue sélectionnée introuvable dans la réponse.")
        except Exception as e:
            st.error(f"Erreur lors du traitement de la traduction : {e}")
