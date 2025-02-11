import uuid

import streamlit as st

from agent import perform_research

st.title("Research")

keywords = st.text_input("Enter keywords")
top_competitors = st.text_input("Enter top competitors")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if st.button("Submit"):
    input_query = f"Keywords: {keywords}, Top Competitors: {top_competitors}"
    response = perform_research(st.session_state.session_id, input_query)
    st.session_state.research_response = response
    st.write(response)
