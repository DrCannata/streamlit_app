import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password", value='')
subject1 = st.sidebar.text_input("Query subject 1", value="Europe")
subject2 = st.sidebar.text_input("Query subject 2", value="Turkey")

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are ",
    )

    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):

        import subprocess
        import json
        result = subprocess.run('"./test.sh" "select \'' + subject1 + '\' as attr union select \'' + subject2 + '\' as attr"', shell=True, stdout=subprocess.PIPE)
        # print(result.stdout)
        json_object = json.loads(result.stdout)
        for i in json_object.get("results"):
            # print(i.get("items"))
            for j in i.get("items"):
                print("j is " + str(j))
                text += j["attr"]

        generate_response(text)
