import streamlit as st
import pandas as pd
from datetime import datetime
from mistralai import Mistral

# Agents disponibles
def get_sentiment(client, prompt):
    try:
        agent_response = client.agents.complete(
            agent_id="ag:56f583a3:20241217:sentiment-n:1be886df",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return agent_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur lors de l'appel à l'agent Sentiment : {e}"

def get_emojibot(client, prompt):
    try:
        agent_response = client.agents.complete(
            agent_id="ag:56f583a3:20241216:emojibot:3a89090a",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return agent_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur lors de l'appel à l'agent Emojibot : {e}"

def get_translation(client, prompt):
    try:
        agent_response = client.agents.complete(
            agent_id="ag:56f583a3:20241217:traduction-n:08c4f0f0",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return agent_response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur lors de l'appel à l'agent Traduction : {e}"

# Demande une clé API dans la sidebar
mistral_api_key = st.sidebar.text_input("Entrez votre clé API", type="password", key="api_key", help="Vous pouvez générer une clé sur le site https://mistral.ai/")

if mistral_api_key:
    if "client" not in st.session_state:
        st.session_state.client = Mistral(api_key=mistral_api_key)
    client = st.session_state.client

    # Menu pour choisir l'agent
    agent_options = {
        "Sentiment": get_sentiment,
        "Emojibot": get_emojibot,
        "Traduction": get_translation
    }
    agent_ids = {
        "Sentiment": "ag:56f583a3:20241217:sentiment-n:1be886df",
        "Emojibot": "ag:56f583a3:20241216:emojibot:3a89090a",
        "Traduction": "ag:56f583a3:20241217:traduction-n:08c4f0f0"
    }
    selected_agent = st.sidebar.selectbox("Choisissez un agent", list(agent_options.keys()), key="selected_agent")

    # Change le titre de la page selon l'agent choisi
    st.title(f"Discussion avec {selected_agent}")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Boutons pour effacer ou sauvegarder l'historique
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("Effacer l'historique"):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("Sauvegarder l'historique"):
            if st.session_state.messages:
                data = []
                for i in range(0, len(st.session_state.messages), 2):
                    user_message = st.session_state.messages[i]["content"]
                    assistant_message = st.session_state.messages[i + 1]["content"] if i + 1 < len(st.session_state.messages) else ""
                    data.append({
                        "agent_name": selected_agent,
                        "agent_id": agent_ids[selected_agent],
                        "prompt": user_message,
                        "reponse": assistant_message
                    })
                df = pd.DataFrame(data)
                timestamp = datetime.now().strftime("%Y%m%d-%H%M")
                csv_filename = f"{timestamp}_historique_chatbot.csv"
                st.sidebar.download_button(
                    label="Télécharger l'historique",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name=csv_filename,
                    mime='text/csv'
                )
                st.sidebar.success("Fichier prêt à télécharger.")
            else:
                st.sidebar.warning("Aucun historique à sauvegarder.")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Que puis-je faire pour vous ?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get response from selected agent
        agent_function = agent_options[selected_agent]
        response = agent_function(client, prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.sidebar.warning("Veuillez entrer une clé API valide pour continuer.")
