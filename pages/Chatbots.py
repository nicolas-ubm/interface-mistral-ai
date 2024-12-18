import streamlit as st
from functions import get_ner
from mistralai import Mistral

st.title("Discussion avec Mistral Agent")

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
    selected_agent = st.sidebar.selectbox("Choisissez un agent", list(agent_options.keys()), key="selected_agent")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

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
