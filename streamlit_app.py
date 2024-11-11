import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
# import oracledb

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

import os


# userpwd = os.environ.get("PYTHON_PASSWORD")

# This was helpful: https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html
# oracledb.init_oracle_client()
# connection = oracledb.connect(user="OMLUSER", password="Cenne#e49Cenne#e49",
#                               host="150.136.183.171", port=1521, service_name="DB23AI_PDB1.sub08201532330.philfnvcn.oraclevcn.com")
# print(connection)

# with connection.cursor() as cursor:
#     for (r,) in cursor.execute("SELECT VECTOR_EMBEDDING(ALL_MINILM_L12_V2 USING pageContent as data) AS embedding FROM Carnot"):
#         print(r)
#         print("")

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
