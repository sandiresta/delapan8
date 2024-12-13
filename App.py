import streamlit as st

st.set_page_config(page_title="Image Processing App", page_icon= r"C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\logo pu.png")

st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate through the app.")

st.write("# Welcome to the Image Processing App")
st.image(r"C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\logo pu.png", width=200, caption="Our Beloved University")
st.write("This is the main page. Use the menu on the left to explore different sections.")
