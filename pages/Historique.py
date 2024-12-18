import streamlit as st
import pandas as pd

# Titre de la page
st.title("Historique du Chatbot")

# Sidebar pour uploader le fichier CSV
uploaded_file = st.sidebar.file_uploader("Charger un fichier CSV", type=["csv"], key="uploaded_csv")

def display_and_edit_csv(file):
    try:
        # Lire le fichier CSV
        df = pd.read_csv(file)
        
        # Affichage des données
        st.subheader("Données de l'historique")
        edited_df = st.experimental_data_editor(df, num_rows="dynamic", key="data_editor")
        
        # Nom par défaut pour enregistrer le fichier
        default_filename = file.name if hasattr(file, 'name') else "historique_chatbot.csv"
        filename = st.text_input("Nom du fichier pour l'enregistrement", value=default_filename, key="save_filename")

        # Bouton pour enregistrer
        if st.button("Enregistrer le fichier"):
            csv_data = edited_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Télécharger le fichier modifié",
                data=csv_data,
                file_name=filename,
                mime="text/csv"
            )
            st.success("Fichier prêt à être téléchargé.")
    except Exception as e:
        st.error(f"Erreur lors du chargement ou de l'affichage du fichier : {e}")

if uploaded_file:
    display_and_edit_csv(uploaded_file)
else:
    st.info("Veuillez charger un fichier CSV pour commencer.")
