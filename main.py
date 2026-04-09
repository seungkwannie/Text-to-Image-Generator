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
            "https://api.stability.ai/v1/generate/stable-diffusion-xl-1024-v1-0",
            headers={"Authorization": f"Bearer {API_KEY}"},
            files={"none": (None, "")},
            data={"text_prompts[0][text]": prompt, "steps": 30, "cfg_scale": 7.0}
        )
        response.raise_for_status()

        import base64
        from io import BytesIO

        # Stability AI returns images in base64 format
        image_data = response.json()["artifacts"][0]["base64"]
        image_bytes = base64.b64decode(image_data)
        image = BytesIO(image_bytes)

        st.write("Image generated successfully!")
        st.image(image, caption="Generated Image")

    except Exception as e:
        st.error(f"Error generating image: {e}")

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
