"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
# import features
from features import form_input
from database import store


st.title("Person Details")
st.subheader("Please enter the following details below:")


with st.form("details_form"):
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    age = st.text_input("Age")
    
    
    submitted = st.form_submit_button("Submit")
    # Every form must have a submit button.
    if form_input.validate_user_input(first_name, last_name, age):
        store.upload_data(first_name, last_name, age)
        if submitted:
            # st.write("First Name :", first_name, "Age :", age)
            st.write("Saving to database")
    else:
        st.write("Please provide valid inputs")






