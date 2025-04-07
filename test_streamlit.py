import streamlit as st

st.title("Simple Streamlit Test")
st.write("This is a basic Streamlit app to test functionality.")

number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")

if st.button("Click Me"):
    st.success("Button was clicked!")