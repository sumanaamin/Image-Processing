import cv2
import streamlit as st
from PIL import Image
import numpy as np

# Set page configuration
st.set_page_config(page_title="Image Processing", layout="centered")

st.title("Image Processing")
st.write("Upload an image to start processing.")

# Initialize session state for toggling
if "show_grayscale" not in st.session_state:
    st.session_state.show_grayscale = False
if "show_bw" not in st.session_state:
    st.session_state.show_bw = False
if "show_resized" not in st.session_state:
    st.session_state.show_resized = False
if "show_cropped" not in st.session_state:
    st.session_state.show_cropped = False

# File uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR", caption="Uploaded Image")

    # Process the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Grayscale
    threshold_value = 127
    _, bw_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)  # Black and White
    width, height = 500, 500
    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)  # Resized Image
    crop_image = image[50:200, 100:300]  # Cropped Image

    # Horizontal alignment for buttons
    st.subheader("Image Processing Options")
    col1, col2, col3, col4 = st.columns(4)  # Create four columns for buttons

    # Grayscale toggle button
    with col1:
        if st.button("Grayscale Image"):
            st.session_state.show_grayscale = not st.session_state.show_grayscale
        if st.session_state.show_grayscale:
            st.image(gray_image, channels="GRAY", caption="Grayscale Image")

    # Black and White toggle button
    with col2:
        if st.button("Black&White Image"):
            st.session_state.show_bw = not st.session_state.show_bw
        if st.session_state.show_bw:
            st.image(bw_image, channels="GRAY", caption="Black and White Image")

    # Resized toggle button
    with col3:
        if st.button("Resized Image"):
            st.session_state.show_resized = not st.session_state.show_resized
        if st.session_state.show_resized:
            st.image(resized, channels="BGR", caption="Resized Image")

    # Cropped toggle button
    with col4:
        if st.button("Cropped Image"):
            st.session_state.show_cropped = not st.session_state.show_cropped
        if st.session_state.show_cropped:
            st.image(crop_image, channels="BGR", caption="Cropped Image")
#else:
  #  st.warning("Please upload an image file to proceed.")
