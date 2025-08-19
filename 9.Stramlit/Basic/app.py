#import streamlit as st
import streamlit as st

#create a title for the app
st.title("My First Streamlit App")

# input from the user
name =  st.text_input("Enter your name:")

#button to submit the name
if st.button("submit"):
    #display the name
    st.write(f"Hello, {name}!")

    # run the app
    # streamlit run app.py


