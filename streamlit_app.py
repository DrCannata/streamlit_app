import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
subject = st.sidebar.text_input("Query subject")

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        # "What are the three key pieces of advice for learning how to code?",
        "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",
    )

    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):

        import subprocess
        import json
        result = subprocess.run('"./test.sh" "select \'' + subject + '\' as attr from dual"', shell=True, stdout=subprocess.PIPE)
        # print(result.stdout)
        json_object = json.loads(result.stdout)
        for i in json_object.get("results"):
            # print(i.get("items"))
            for j in i.get("items"):
                # print("j is " + str(j))
                text += j["attr"]

        generate_response(text)
