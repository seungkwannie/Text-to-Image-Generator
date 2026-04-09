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

    # UPDATED: Use the modern Stable Image Ultra or Core endpoint
    # 'ultra' is the highest quality; you can also use 'core'
    url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"

    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "application/json"
            },
            files={"none": (None, "")},  # Required for multipart/form-data
            data={
                "prompt": prompt,
                "output_format": "webp"  # You can use 'png' or 'jpeg' too
            }
        )

        response.raise_for_status()


        # The new V2 API returns 'image' instead of 'artifacts'
        image_data = response.json()["image"]
        image_bytes = base64.b64decode(image_data)

        st.success("Image generated successfully!")
        st.image(image_bytes, caption="Generated Image")

    except Exception as e:
        st.error(f"Error: {e}")

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
