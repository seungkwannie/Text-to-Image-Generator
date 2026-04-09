import streamlit as st

API_KEY = "sk-NQc71APpFfjKF5zXP1EGOyjjmvwNsDmzCSPuskTTA1tjw6cx"

st.title("🎨 Text to Image Generator")
st.divider()

prompt = st.text_input("Enter your image description: ")

st.write("Example prompts:")
st.write("""
    * **A cute robot** painting a picture
    * **A futuristic city** with flying cars
    * **A cozy coffee shop** on a rainy day
""")


def generate_image():
    pass

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
