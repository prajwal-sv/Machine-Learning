#import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np

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


# slideer
st.subheader("Slider Example")
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# checkbox
st.subheader("Checkbox Example")
checkbox_value = st.checkbox("Check me!")
if checkbox_value:
    st.write("Checkbox is checked!")

#  display a line chart
st.subheader("Line Chart Example")

dataframe= pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10),
    'Column 3': np.random.randn(10)})

st.write("here is dataframe:")
st.dataframe(dataframe)

st.line_chart(dataframe)


