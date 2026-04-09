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

    # You must specify WHICH model you want to use in the URL itself
    engine_id = "stable-diffusion-xl-1024-v1-0"
    url = f"https://api.stability.ai/v1/engines/{engine_id}/text-to-image"

    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "application/json",  # Tells the server you want JSON back
            },
            # Use 'json=' instead of 'data=' for easier formatting with Stability
            json={
                "text_prompts": [{"text": prompt}],
                "cfg_scale": 7,
                "steps": 30,
            }
        )

        response.raise_for_status()

        import base64
        from io import BytesIO

        # Stability AI returns a list of artifacts
        response_data = response.json()
        image_data = response_data["artifacts"][0]["base64"]
        image_bytes = base64.b64decode(image_data)

        st.success("Image generated successfully!")
        st.image(image_bytes, caption="Generated Image")

    except Exception as e:
        # This will now show the actual error message from the server if it fails
        st.error(f"Error generating image: {e}")

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
