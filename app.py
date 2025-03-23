import streamlit as st
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
import threading
import time
import sys
import os
import base64
import tempfile
import json

# Import your modules
from styles import apply_styles
from views import (
    display_search_view,
    display_results_view,
    display_language_view,
    display_audio_view
)
from news import get_news_articles
from sentiment import process_news_articles
from text_to_speech import text_to_speech
from language import translate_summary, LANGUAGE_CODES

# Initialize FastAPI
api = FastAPI(title="News Analysis API")
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define API models
class NewsRequest(BaseModel):
    company_name: str

class LanguageRequest(BaseModel):
    processed_data: Dict[str, Any]
    language_code: str

class NewsResponse(BaseModel):
    processed_data: Dict[str, Any]

class AudioResponse(BaseModel):
    audio_file: str
    summary_text: str
    language_name: str

# API routes
@api.post("/api/news", response_model=NewsResponse)
async def analyze_news(request: NewsRequest):
    """Get and analyze news articles for a company"""
    try:
        # Get news articles
        news_articles = get_news_articles(request.company_name)
        
        if not news_articles:
            raise HTTPException(status_code=404, detail="No news articles found for this company")
        
        # Process articles with sentiment and topic analysis
        processed_data = process_news_articles(request.company_name, news_articles)
        
        return {"processed_data": processed_data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api.post("/api/audio", response_model=AudioResponse)
async def generate_audio(request: LanguageRequest):
    """Generate audio summary in specified language"""
    try:
        # Get language information
        language_code = request.language_code
        language_name = next((lang["name"] for lang in LANGUAGE_CODES.values() 
                             if lang["code"] == language_code), "English")
        
        # Generate summary in selected language
        summary_text = translate_summary(request.processed_data, language_code)
        
        # Create a temporary file with a unique name
        temp_dir = os.path.join(tempfile.gettempdir(), "news_audio")
        os.makedirs(temp_dir, exist_ok=True)
        audio_file = os.path.join(temp_dir, f"speech_{language_code}_{hash(json.dumps(request.processed_data))}.mp3")
        
        # Convert the translated summary to speech
        audio_path = text_to_speech(summary_text, language_code, audio_file)
        
        return {
            "audio_file": audio_path,
            "summary_text": summary_text,
            "language_name": language_name
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define a function to run FastAPI in a separate thread
def run_api():
    uvicorn.run(api, host="0.0.0.0", port=8000)

# Start FastAPI in a thread when script is run
api_thread = threading.Thread(target=run_api, daemon=True)
api_thread.start()

# Wait for API to start
time.sleep(2)

# Download required NLTK resources
import nltk
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Download SpaCy model
import spacy
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

# Function to handle navigation between stages
def set_stage(stage):
    """
    Set the current stage in the application flow
    
    Parameters:
    stage (str): New stage name ('search', 'results', 'language', or 'audio')
    """
    st.session_state.current_stage = stage

# Main Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="News Sentiment Analyzer",
        page_icon="📰",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom CSS
    apply_styles()
    
    # Initialize session state for storing data between reruns
    if 'processed_data' not in st.session_state:
        st.session_state.processed_data = None
    if 'current_stage' not in st.session_state:
        st.session_state.current_stage = "search"  # Possible values: search, results, language, audio
    if 'audio_data' not in st.session_state:
        st.session_state.audio_data = None
    
    # Main app title
    st.markdown('<div class="title">📰 News Sentiment Analyzer</div>', unsafe_allow_html=True)
    
    # Display appropriate view based on current state
    if st.session_state.current_stage == "search":
        display_search_view("/api", set_stage)  # Note: Changed API_URL to "/api"
    elif st.session_state.current_stage == "results":
        display_results_view(set_stage)
    elif st.session_state.current_stage == "language":
        display_language_view("/api", set_stage)  # Note: Changed API_URL to "/api"
    elif st.session_state.current_stage == "audio":
        display_audio_view(set_stage)

if __name__ == "__main__":
    main()