import streamlit as st
import requests
import base64
import time

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

def download_image():
    pass


def generate_image():
    if not prompt:
        st.warning("Please enter a description.")
        return

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }

    max_retries = 3
    retry_delay = 5  # Default wait time in seconds

    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)

            # If we hit the rate limit (429)
            if response.status_code == 429:
                # Try to get wait time from server, otherwise use default
                wait_time = int(response.headers.get("Retry-After", retry_delay))
                st.info(f"Rate limited. Retrying in {wait_time}s... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue  # Try the loop again

            response.raise_for_status()  # Catch other errors (401, 404, 500)

            # Success! Process the image
            image_data = response.json()["artifacts"][0]["base64"]
            image_bytes = base64.b64decode(image_data)
            st.success("Image generated successfully!")
            st.image(image_bytes, caption="Generated Image")
            return  # Exit function on success

        except requests.exceptions.HTTPError as e:
            if response.status_code == 402:
                st.error("Error: You have run out of Stability AI credits!")
            else:
                st.error(f"API Error: {e}")
            break  # Stop retrying for non-429 errors
        except Exception as e:
            st.error(f"Unexpected Error: {e}")
            break

# def generate_image():
#     if not prompt:
#         st.warning("Please enter a description to generate an image.")
#         return
#
#     url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
#
#     try:
#         payload = {
#             "text_prompts": [
#                 {
#                     "text": prompt,
#                     "weight": 1
#                 }
#             ],
#             "cfg_scale": 7,
#             "height": 1024,
#             "width": 1024,
#             "samples": 1,
#             "steps": 30,
#         }
#
#         headers = {
#             "Accept": "application/json",
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {API_KEY}",
#         }
#
#         response = requests.post(url, json=payload, headers=headers)
#
#         response.raise_for_status()
#
#         image_data = response.json()["artifacts"][0]["base64"]
#         image_bytes = base64.b64decode(image_data)
#
#         st.success("Image generated successfully!")
#         st.image(image_bytes, caption="Generated Image")
#
#         st.button("Download Image", on_click=download_image)
#
#     except Exception as e:
#         st.error(f"Error: {e}")

# def generate_image():
#     if st.button("Generate Image"):
#         if not prompt:
#             st.warning("Please enter a description.")
#         else:
#             with st.spinner("Generating..."):
#                 try:
#                     image_b64 = generate_image()
#                     if image_b64:
#                         image_bytes = base64.b64decode(image_b64)
#                         st.image(image_bytes, caption="Generated Image")
#
#                         st.session_state['last_image'] = image_bytes
#                 except Exception as e:
#                     st.error(f"Error: {e}")
#
#     url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
#
#     payload = {
#         "text_prompts": [{"text": prompt, "weight": 1}],
#         "cfg_scale": 7,
#         "height": 1024,
#         "width": 1024,
#         "samples": 1,
#         "steps": 30,
#     }
#
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {API_KEY}",
#     }
#
#     response = requests.post(url, json=payload, headers=headers)
#
#     if response.status_code == 429:
#         st.error("Rate limit exceeded. Please wait 60 seconds.")
#         return None
#
#     response.raise_for_status()
#     return response.json()["artifacts"][0]["base64"]

st.button("Generate Image", on_click=generate_image)
