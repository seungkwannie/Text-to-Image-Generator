import streamlit as st
import requests
import base64

API_KEY = "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

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

    url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"

    try:
        payload = {
            "prompt": (None, prompt),
            "output_format": (None, "png"),
            "aspect_ratio": (None, "1:1")
        }

        headers = {
            "Accept": "image/*",
            "Authorization": f"Bearer {API_KEY}",
        }

        response = requests.post(url, headers=headers, files=payload)

        if response.status_code != 200:
            st.error(f"API Error {response.status_code}: {response.text}")
            return

        image_bytes = response.content

        st.success("Image generated successfully!")
        st.image(image_bytes, caption="Generated Image")

        st.download_button(
            label="Download Image",
            data=image_bytes,
            file_name="generated_ultra.png",
            mime="image/png"
        )

    except Exception as e:
        st.error(f"Error: {e}")


def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
