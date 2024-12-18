import streamlit as st
from functions import get_ner, 
from mistralai import Mistral


# Agents disponibles

def get_emojibot(client, prompt):
    agent_response = client.agents.complete(
        agent_id="ag:56f583a3:20241216:emojibot:3a89090a",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return eval(agent_response.choices[0].message.content)

def get_sentiment(client, prompt):
    agent_response = client.agents.complete(
        agent_id="ag:56f583a3:20241217:sentiment-n:1be886df",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return eval(agent_response.choices[0].message.content)

def get_translation(client, prompt):
    agent_response = client.agents.complete(
        agent_id="ag:56f583a3:20241217:traduction-n:08c4f0f0",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return eval(agent_response.choices[0].message.content)



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
