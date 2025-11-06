import streamlit as st
st.write("Kelompok : 18")
st.markdown("""
- Deva Lubna Listya		(0110222258)
- Apriyanto			    (0110222256)
- Raydino Situmeang		(0110222278)
""")
st.write("Images")

#images
import streamlit as st
import base64
from PIL import Image

st.write("Displaying images")
st.image("../assets/image.jpg")
st.write("Image courtesy: Unsplash")

# Displaying multiple images
animal_images = [
    '../assets/kucing1.jpg',
    '../assets/kucing2.jpg',
    '../assets/kucing3.jpg',
    '../assets/kucing4.jpg',
]
st.image(animal_images, width=150)
st.write("Image Courtesy: Unsplash")

# ✅ Add background image (eror jadi chatgpt^^)
def add_local_background_image(image_path):
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

st.write("Background Image")
add_local_background_image('../assets/panda.jpg')

# Resizing image
original_image = Image.open("../assets/angsa.jpg")
st.title("Original Image")
st.image(original_image)

resized_image = original_image.resize((600, 400))
st.title("Resized Image")
st.image(resized_image)
