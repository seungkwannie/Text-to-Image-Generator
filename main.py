import streamlit as st
import requests
import base64

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

    # 1. The V2 Ultra URL is correct
    url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"

    try:
        # 2. Simplified V2 Payload
        # Note: 'height' and 'width' are not used here.
        # You use 'aspect_ratio' instead (e.g., "1:1", "16:9").
        payload = {
            "prompt": (None, prompt),
            "output_format": (None, "png"),
            "aspect_ratio": (None, "1:1")
        }

        # 3. Correct V2 Headers
        # REMOVE "Content-Type". The 'requests' library adds the correct one automatically.
        headers = {
            "Accept": "image/*",  # This tells the API to send back the actual image file
            "Authorization": f"Bearer {API_KEY}",
        }

        # 4. Use 'files' instead of 'data' or 'json'
        response = requests.post(url, headers=headers, files=payload)

        # This will give you a descriptive error if something is still wrong
        if response.status_code != 200:
            st.error(f"API Error {response.status_code}: {response.text}")
            return

        # 5. Handle Response
        # Since we used "Accept: image/*", the image is in response.content
        image_bytes = response.content

        st.success("Image generated successfully!")
        st.image(image_bytes, caption="Generated Image")

        # Download button (Standard Streamlit way)
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
