import streamlit as st
import pandas as pd
import json

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
        edited_df = st.data_editor(df, num_rows="dynamic", key="data_editor")
        
        # Nom par défaut pour enregistrer le fichier CSV
        default_csv_filename = file.name if hasattr(file, 'name') else "historique_chatbot.csv"
        csv_filename = st.text_input("Nom du fichier CSV pour l'enregistrement", value=default_csv_filename, key="save_csv_filename")

        # Nom par défaut pour enregistrer le fichier JSONL
        default_jsonl_filename = file.name.replace('.csv', '.jsonl') if hasattr(file, 'name') else "historique_chatbot.jsonl"
        jsonl_filename = st.text_input("Nom du fichier JSONL pour l'enregistrement", value=default_jsonl_filename, key="save_jsonl_filename")

        # Bouton pour enregistrer en CSV
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        if st.button("Enregistrer en CSV"):
            csv_data = convert_df_to_csv(edited_df)
            st.download_button(
                label="Télécharger le fichier modifié en CSV",
                data=csv_data,
                file_name=csv_filename,
                mime="text/csv"
            )
            st.success("Fichier CSV prêt à être téléchargé.")

        # Bouton pour enregistrer en JSONL
        def convert_df_to_jsonl(df):
            jsonl_data = ""
            for _, row in df.iterrows():
                messages = [
                    {"role": "user", "content": row["prompt"]},
                    {"role": "assistant", "content": row["reponse"]}
                ]
                jsonl_data += json.dumps({"messages": messages}) + "\n"
            return jsonl_data.encode('utf-8')

        if st.button("Enregistrer en JSONL"):
            jsonl_data = convert_df_to_jsonl(edited_df)
            st.download_button(
                label="Télécharger le fichier modifié en JSONL",
                data=jsonl_data,
                file_name=jsonl_filename,
                mime="application/json"
            )
            st.success("Fichier JSONL prêt à être téléchargé.")
    except Exception as e:
        st.error(f"Erreur lors du chargement ou de l'affichage du fichier : {e}")

if uploaded_file:
    display_and_edit_csv(uploaded_file)
else:
    st.info("Veuillez charger un fichier CSV pour commencer.")
