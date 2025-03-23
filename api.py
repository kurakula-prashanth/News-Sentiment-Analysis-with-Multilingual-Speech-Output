import requests
import streamlit as st
import os
import base64

def call_api(endpoint, data):
    """
    Makes API calls to the backend
    
    Parameters:
    endpoint (str): API endpoint path (e.g., '/api/news')
    data (dict): JSON data to send
    
    Returns:
    dict: API response data
    """
    # For Hugging Face Spaces, we use relative URLs instead of localhost:8000
    url = f"{endpoint}"
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {str(e)}")
        return None

def get_audio_data(audio_file_path):
    """
    Get base64 encoded audio data from file
    
    Parameters:
    audio_file_path (str): Path to audio file
    
    Returns:
    str: Base64 encoded audio data
    """
    try:
        # Check if file exists
        if not os.path.exists(audio_file_path):
            st.error(f"Audio file not found: {audio_file_path}")
            return None
            
        # Read and encode audio file
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
            return audio_base64
    except Exception as e:
        st.error(f"Error loading audio: {str(e)}")
        return None