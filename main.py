import nltk
import os
import spacy
from news import get_news_articles
from sentiment import process_news_articles
from text_to_speech import generate_speech_for_analysis

# Download NLTK resources (only needed once)
home_dir = os.getenv("USERPROFILE")  # On Windows, use USERPROFILE instead of HOME
nltk.data.path.append(os.path.join(home_dir, "nltk_data"))

# Load SpaCy model (run once)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def display_results(processed_data):
    """Display detailed results in English"""
    company_name = processed_data["Company"]
    print(f"\nAnalysis Results for {company_name}:\n")
    
    print("News Articles:")
    for i, article in enumerate(processed_data["Articles"], 1):
        # Display full title
        print(f"{i}. {article['Title']}")
        print(f"   Summary: {article['Summary']}")
        print(f"   Sentiment: {article['Sentiment']}")
        print(f"   Topics: {', '.join(article['Topics'])}")
        print("---")
    
    print("\nSentiment Distribution:")
    distribution = processed_data["Comparative Sentiment Score"]["Sentiment Distribution"]
    print(f"   Positive: {distribution['Positive']}")
    print(f"   Negative: {distribution['Negative']}")
    print(f"   Neutral: {distribution['Neutral']}")
    
    print("\nCoverage Differences:")
    for comparison in processed_data["Comparative Sentiment Score"]["Coverage Differences"]:
        print(f"   - {comparison['Comparison']}")
        print(f"     Impact: {comparison['Impact']}")
    
    print("\nTopic Overlap:")
    topic_overlap = processed_data["Comparative Sentiment Score"]["Topic Overlap"]
    if topic_overlap["Common Topics"]:
        print(f"   Common Topics: {', '.join(topic_overlap['Common Topics'])}")
    else:
        print("   Common Topics: None")
    
    print("\nFinal Sentiment Analysis:")
    print(f"   {processed_data['Final Sentiment Analysis']}")

if __name__ == "__main__":
    company_name = input("Enter the company you want to know: ")
    news_articles = get_news_articles(company_name)
    
    # Process articles with sentiment and topic analysis
    processed_data = process_news_articles(company_name, news_articles)
    
    # Display detailed results in English
    display_results(processed_data)
    
    # Generate speech in user's chosen language
    audio_file, summary_text, language_name = generate_speech_for_analysis(processed_data)
    
    print(f"\n{language_name} speech saved to: {audio_file}")
    print("You can play this file using any media player.")