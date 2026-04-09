import streamlit as st
import requests

API_KEY = "sk-NQc71APpFfjKF5zXP1EGOyjjmvwNsDmzCSPuskTTA1tjw6cx"

st.title("🎨 Text to Image Generator")
st.divider()

prompt = st.text_area("Enter your image description:")

st.write("**Example prompts:**")
st.markdown("""
• A cute robot painting a picture

• A futuristic city with flying cars

• A cozy coffee shop on a rainy day
""")

st.markdown("""
<style>
    div.stButton > button {
        background-color: #ff5a5f;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
    }
    div.stButton > button:hover {
        background-color: #ff7e82;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def generate_image():
    if not prompt:
        st.warning("Please enter a description to generate an image.")
        return

    try:
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": "dall-e-3", "prompt": prompt, "n": 1, "size": "512x512"}
        )
        response.raise_for_status()
        image_url = response.json()["data"][0]["url"]

        st.write("Image generated successfully!")
        st.image(image_url, caption="Generated Image")

    except Exception as e:
        st.error(f"Error generating image: {e}")

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
