import tempfile
import os
from gtts import gTTS
from IPython.display import Audio, display
from language import translate_summary, LANGUAGE_CODES

def text_to_speech(text, language_code, output_file=None):
    """
    Convert text to speech using gTTS in the specified language
    
    Parameters:
    text (str): Text to convert to speech
    language_code (str): Language code for gTTS
    output_file (str, optional): Path to save the audio file. If None, a temporary file will be created.
    
    Returns:
    str: Path to the generated audio file
    """
    # If no output file is specified, create a temporary file
    if output_file is None:
        temp_dir = tempfile.gettempdir()
        output_file = os.path.join(temp_dir, f"speech_{language_code}.mp3")
    
    # Create gTTS object with specified language
    tts = gTTS(text=text, lang=language_code, slow=False)
    
    # Save the audio file
    tts.save(output_file)
    
    return output_file


def generate_speech_for_analysis(processed_data):
    """
    Generate speech for the analysis results in the user's chosen language
    
    Parameters:
    processed_data (dict): The processed news data with sentiment analysis
    
    Returns:
    str: Path to the generated audio file
    """
    # Display language options
    print("\nSelect language for audio output:")
    for key, lang in LANGUAGE_CODES.items():
        print(f"{key}. {lang['name']}")
    
    # Get user choice
    while True:
        language_choice = input("Enter your choice (1-6): ")
        if language_choice in LANGUAGE_CODES:
            break
        print("Invalid choice. Please try again.")
    
    selected_language = LANGUAGE_CODES[language_choice]
    language_name = selected_language["name"]
    language_code = selected_language["code"]
    
    print(f"\nGenerating {language_name} speech...")
    
    # Generate summary in selected language
    summary_text = translate_summary(processed_data, language_code)
    
    # Convert the translated summary to speech
    audio_file = text_to_speech(summary_text, language_code)
    
    print(f"\n{language_name} summary text:")
    print(summary_text)
    
    return audio_file, summary_text, language_name
