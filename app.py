import openai
import streamlit as st
from streamlit_chat import message
from driver import read_query
from train_cypher import examples
from openaigpt4 import generate_cypher

st.set_page_config(page_title="Search Neo4j")
st.title("Neo4j POC")

openai.api_key = ''

def generate_response(prompt, cypher=True):
    usr_input = [{"role": "user", "content": prompt}]
    cypher_query = generate_cypher(usr_input)
    message = read_query(cypher_query)
    return message, cypher_query

    
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
            st.write(message["content"])

if user_input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
            st.write(user_input)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response,cypher_query = generate_response(user_input) 
        message = {"role": "assistant", "content": response}
        if "MATCH" in cypher_query:
            st.write(cypher_query)
        st.write(message["content"]) 
        st.session_state.messages.append(message)