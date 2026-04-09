import streamlit as st
import requests
import pandas as pd
import numpy as np

API_KEY = "sk-NQc71APpFfjKF5zXP1EGOyjjmvwNsDmzCSPuskTTA1tjw6cx"

st.title("🎨 Text to Image Generator")
st.write("---------------------------------------------------------------------")

prompt = st.text_input("Enter your image description: ")

Examples = st.write("Example prompts:"
                    "\n• A cute robot painting a picture"
                    "\n• A futuristic city with flying cars"
                    "\n• A cozy coffee shop on a rainy day")

def generate_image():
    pass

def download_image():
    pass

st.button("Generate Image", on_click=generate_image)
