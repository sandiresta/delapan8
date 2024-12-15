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
# UPLOAD IMAGE CONTENT
with tab3:
    # VALIDATION IMAGE
    def validate_image(image):
        try:
            img = Image.open(image)
            img.verify() 
        except Exception as e:
            st.error("Invalid image file. Please upload a valid image file (.jpg, .jpeg, .png).")
            return False

        # Check file type
        if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            st.error("Invalid file type. Please upload a .jpg, .jpeg, or .png image.")
            return False

        # Check size
        max_size_MB = 2  # 2 MB
        max_size_bytes = max_size_MB * 1024 * 1024  # 2 MB in bytes
        if image.size > max_size_bytes:
            st.error(f"File size too large. Maximum allowed size is {max_size_MB} MB.")
            return False

        # Check dimensions
        img_width, img_height = img.size
        min_dim = 100  # Minimum dimension (width / height)
        max_dim = 2000  # Maximum dimension (width / height)
        if img_width < min_dim or img_width > max_dim or img_height < min_dim or img_height > max_dim:
            st.error(f"Invalid image dimensions. Image dimensions should be between {min_dim}x{min_dim} and {max_dim}x{max_dim} pixels.")
            return False
        return True

