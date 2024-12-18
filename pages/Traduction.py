import streamlit as st
from functions import *
from mistralai import Mistral


st.title('Traduction')
API_KEYS = st.sidebar.text_input("Quel est votre clé API Mistral ?")
client = Mistral(api_key = API_KEYS)

prompt = st.text_area("Prompt :")

response = get_ner(client, prompt)
st.write(response)
