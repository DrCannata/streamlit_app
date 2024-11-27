import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text).content)

with st.form("my_form"):
    text = st.text_area(
        "Initial propmt:",
        "What is the Carnot Project architecture"
        #"Based on this dataset of movies that customers have watched, containing customer IDs, movie IDs and date watched, Which customer has watched the most movies? And how many movies did the others watch?"
        )

    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):

        import subprocess
        import json
        graphQuery = """
            SELECT *
            FROM GRAPH_TABLE( CUSTOMER_WATCHED_MOVIES
                MATCH (c1 IS CUSTOMER)-[e1 IS WATCHED]->(m IS MOVIE)
                COLUMNS (c1.CUST_ID as customer_id, m.MOVIE_ID as movie_id, e1.DAY_ID as date_watched) 
            )
            """
        vectorQuery = """
            SELECT seg
            FROM segs
            ORDER BY vector_distance(vec, (SELECT vector_embedding(ALL_MINILM_L12_V2 using \' """ + text + """\' as data)), COSINE)
            FETCH FIRST 2 ROWS ONLY
            """
        result = subprocess.run("./test.sh \"" + vectorQuery + "\"", shell=True, stdout=subprocess.PIPE)
        print(json.loads(result.stdout))
        text += str(json.loads(result.stdout))
        generate_response(text)