# News Sentiment Analysis with Multilingual Speech Output

## Project Overview

This project is a news sentiment analysis tool that scrapes recent news articles about a specified company, analyzes the sentiment of those articles, extracts key topics, and provides a comprehensive analysis. The tool can then deliver this analysis as speech output in multiple Indian languages (Telugu, Hindi, English, Malayalam, Tamil, or Kannada).

## I have deployed this project in Hugging Face
For deploying in Hugging Face I have created a seaparate files u can download the files from there
The project is deployed and can be accessed [Hugging Face deployment Link](https://huggingface.co/spaces/kurakula-Prashanth2004/News-Sentiment-Analysis-with-Multilingual-Speech-Output).

## Features

- **News Scraping**: Scrapes recent news articles from Bing search results
- **Sentiment Analysis**: Uses both TextBlob and VADER for robust sentiment classification
- **Topic Extraction**: Identifies key topics from articles using NLP techniques
- **Comparative Analysis**: Compares sentiment across articles to identify trends
- **Multilingual Support**: Generates summaries in 6 languages (Telugu, Hindi, English, Malayalam, Tamil, Kannada)
- **Text-to-Speech**: Converts analysis into spoken audio in the selected language
- **Interactive Web Interface**: User-friendly Streamlit interface with responsive design

## Installation

### Using requirements.txt

A requirements.txt file is included to simplify dependency installation:

```bash
# Clone the repository
git clone https://github.com/yourusername/news-sentiment-analysis.git
cd news-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Download required NLTK and SpaCy resources
python -c "import nltk; nltk.download('vader_lexicon'); import os; os.system('python -m spacy download en_core_web_sm')"
```

### Requirements Details

The project requires the following dependencies (specified in requirements.txt):

```
# Core Dependencies
streamlit>=1.23.0
fastapi>=0.100.0
uvicorn>=0.22.0
pydantic>=2.0.0

# Web Scraping and HTTP
requests>=2.31.0
beautifulsoup4>=4.12.0

# NLP and Text Processing
nltk>=3.8.1
textblob>=0.17.1
spacy>=3.6.0
vaderSentiment>=3.3.2

# Data Processing and Visualization
pandas>=2.0.0
plotly>=5.15.0

# Text-to-Speech
gTTS>=2.3.2

# Additional Utils
python-multipart>=0.0.6
aiofiles>=23.1.0
```

## Project Structure

### Core Files
- **app.py**: Main Streamlit application entry point that sets up the page configuration and manages application state
- **api.py**: FastAPI backend that handles news retrieval, analysis, and audio generation
- **views.py**: UI components and view logic for different stages of the application flow
- **utils.py**: Helper functions for API communication and data fetching
- **styles.py**: Custom CSS styling for the Streamlit interface
- **requirements.txt**: List of all dependencies needed to run the project

### Backend Components
- **news.py**: Handles scraping of news articles
- **sentiment.py**: Performs sentiment analysis and topic extraction
- **language.py**: Contains translation functions and language code mappings
- **text_to_speech.py**: Handles text-to-speech conversion

## Application Flow

The application follows a four-stage flow:

1. **Search Stage**: User enters a company name to analyze
2. **Results Stage**: Displays sentiment analysis results, charts, and article summaries
3. **Language Selection Stage**: User selects a language for audio summary
4. **Audio Stage**: Plays audio summary and displays text version

## How to Use

### Running the Web Application

1. Start the FastAPI backend:
   ```
   python api.py
   ```

2. In a separate terminal, start the Streamlit frontend:
   ```
   streamlit run app.py
   ```

3. Navigate to the provided local URL (typically http://localhost:8501)

4. Enter a company name and follow the interactive workflow

### Using the API Directly

The FastAPI backend provides two main endpoints:

1. `/api/news` - Retrieve and analyze news for a company:
   ```python
   import requests
   response = requests.post("http://localhost:8000/api/news", json={"company_name": "Tesla"})
   data = response.json()
   ```

2. `/api/audio` - Generate audio summary in a specific language:
   ```python
   import requests
   response = requests.post("http://localhost:8000/api/audio", 
                           json={"processed_data": data["processed_data"], 
                                "language_code": "en-US"})
   audio_data = response.json()
   ```

## UI Components

The Streamlit interface includes:

- **Search View**: Company name input and analyze button
- **Results View**: 
  - Sentiment distribution pie chart
  - Sentiment count cards (Positive, Negative, Neutral)
  - Overall analysis summary
  - Common topics section
  - Detailed article cards with sentiment-based styling
- **Language Selection**: Buttons for different language options
- **Audio Player**: Audio controls and text summary display

## Styling

The application uses a dark theme with custom styling for:
- Cards with sentiment-specific color coding
- Responsive layout with centered elements
- Custom typography for titles and subtitles
- Interactive elements with consistent styling

## Extending the Project

### Adding New Languages

To add support for additional languages:

1. Update the `LANGUAGE_CODES` dictionary in `language.py` and `views.py`
2. Add appropriate translation functions in `translate_sentiment_analysis()`
3. Add a new language-specific summary generator in `translate_summary()`

### Improving the UI

The current implementation uses Streamlit. To enhance the UI:

- Add more interactive charts (time series, topic relationships)
- Implement user authentication for saved searches
- Add export functionality for reports
- Create a dashboard view for company comparison

### Improving Sentiment Analysis

The current implementation uses both TextBlob and VADER. To improve accuracy:

- Add machine learning-based sentiment analysis models
- Implement aspect-based sentiment analysis
- Consider using pre-trained transformers like BERT

## Troubleshooting

- **NLTK Data Issues**: Ensure NLTK data is downloaded correctly. The script attempts to download it if not found.
- **SpaCy Model Issues**: If the SpaCy model fails to load, the script will try to download it automatically.
- **Web Scraping Issues**: If you encounter problems with article retrieval, check your internet connection or update the user-agent header in `news.py`.
- **API Connection Errors**: Verify that both the FastAPI backend and Streamlit frontend are running and communicating properly.
- **Dependency Issues**: If you encounter package conflicts, try creating a virtual environment before installing requirements.

## License

This project is available for personal and educational use.

## Acknowledgments

- NLTK for natural language processing tools
- TextBlob for sentiment analysis
- SpaCy for topic extraction
- gTTS for text-to-speech conversion
- Streamlit for the interactive web interface
- FastAPI for the backend API
- Plotly for data visualization
