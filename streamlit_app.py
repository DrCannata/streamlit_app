import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )

    import subprocess
    import json
    result = subprocess.run('"./test.sh" "select \'Quantum Mechanics\' from dual"', shell=True, stdout=subprocess.PIPE)
    print(result.stdout)
    json_object = json.loads(result.stdout)
    print(type(json_object))
    #print(json_object.get("results".get("items")))
    my_string = ', '.join(json_object) 
    print(my_string)
    text += my_string + " for 2020 election"
    print(text)

    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
