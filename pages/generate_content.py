import streamlit as st

from agent import generate_content

st.title("Content Generation")

try:
    research_response = st.session_state.research_response
except:
    st.warning("Generate research response first")


image_urls = st.text_input("Enter image URLs")
if st.button("Submit"):
    input_query = f"Image URLs: {image_urls}, Research Response: {research_response}"
    response = generate_content(st.session_state.session_id, input_query)
    st.session_state.content_response = response
    st.write(response)
