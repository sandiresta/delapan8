import streamlit as st
from PIL import Image, ImageEnhance

st.title("Image Processing Application")
st.write("Upload an image to apply filters and enhancements.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Brightness adjustment
    brightness = st.slider("Adjust Brightness", 0.5, 3.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(brightness)
    st.image(brightened_image, caption="Brightened Image", use_column_width=True)

    # Grayscale filter
    if st.checkbox("Convert to Grayscale"):
        grayscale_image = image.convert("L")
        st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)
