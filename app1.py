import streamlit as st

st.title("Welcome to App😎")
st.markdown("This is the main application page.")
user_name = st.text_input("Name")
user_age = st.slider("Age")
submit_button = st.button("Submit")
if submit_button:
    st.markdown(f"Hello {user_name}, you are {user_age} years old!")