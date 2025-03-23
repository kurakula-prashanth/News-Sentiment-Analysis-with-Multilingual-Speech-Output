import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import spacy
from collections import Counter


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


def analyze_sentiment(text):
    # Using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Using VADER
    sid = SentimentIntensityAnalyzer()
    vader_scores = sid.polarity_scores(text)
    
    # Combine both approaches for more robust analysis
    if polarity > 0.1 or vader_scores['compound'] > 0.05:
        return "Positive"
    elif polarity < -0.1 or vader_scores['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

def extract_topics(text, num_topics=3):
    # Process with SpaCy
    doc = nlp(text)
    
    # Extract named entities
    entities = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "EVENT", "GPE", "WORK_OF_ART"]]
    
    # Extract key noun phrases
    noun_phrases = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) > 1]
    
    # Extract keywords using frequency
    words = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop and len(token.text) > 3]
    word_freq = Counter(words)
    keywords = [word for word, count in word_freq.most_common(5)]
    
    # Combine and select unique topics
    all_potential_topics = entities + noun_phrases + keywords
    
    # Clean and deduplicate topics
    clean_topics = []
    seen = set()
    for topic in all_potential_topics:
        topic = topic.strip().title()
        
        # Skip short topics and common articles/determiners
        if not topic or len(topic) < 4 or topic.lower() in ['the', 'this', 'that', 'these', 'those', 'already', 'an']:
            continue
            
        # Remove articles from the beginning
        if topic.lower().startswith('a ') or topic.lower().startswith('an ') or topic.lower().startswith('the '):
            topic = topic[topic.find(' ')+1:]
        
        # Add to clean topics if not seen before
        if topic.lower() not in seen and len(topic) > 3:
            seen.add(topic.lower())
            clean_topics.append(topic)
    
    # If we don't have enough topics, try to get the main subject
    if not clean_topics and len(text) > 0:
        # Try to extract the company or main subject from the text
        for token in doc:
            if token.pos_ == "PROPN" and len(token.text) > 3 and token.text.lower() not in seen:
                seen.add(token.text.lower())
                clean_topics.append(token.text.title())
                if len(clean_topics) >= num_topics:
                    break
    
    return clean_topics[:num_topics]

def perform_comparative_analysis(articles):
    # Calculate sentiment distribution
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment_counts[article["Sentiment"]] += 1
    
    # Find all topics across articles
    all_topics = set()
    for article in articles:
        all_topics.update(article["Topics"])
    
    # Find topic overlap
    topic_frequency = {topic: 0 for topic in all_topics}
    for article in articles:
        for topic in article["Topics"]:
            topic_frequency[topic] += 1
    
    common_topics = [topic for topic, count in topic_frequency.items() if count > 1]
    
    # Generate comparisons between articles
    comparisons = []
    if len(articles) >= 2:
        for i in range(len(articles)-1):
            for j in range(i+1, min(i+3, len(articles))):
                article1 = articles[i]
                article2 = articles[j]
                
                # Skip if both articles have the same sentiment
                if article1["Sentiment"] == article2["Sentiment"]:
                    continue
                
                # Get short version of titles for comparison (first 40 chars)
                title1 = article1["Title"][:40] + "..." if len(article1["Title"]) > 40 else article1["Title"]
                title2 = article2["Title"][:40] + "..." if len(article2["Title"]) > 40 else article2["Title"]
                
                comparison = {
                    "Comparison": f"Article '{title1}' has {article1['Sentiment'].lower()} sentiment, while '{title2}' has {article2['Sentiment'].lower()} sentiment.",
                    "Impact": generate_impact_statement(article1, article2)
                }
                comparisons.append(comparison)
    
    # Limit to most significant comparisons
    comparisons = comparisons[:3]
    
    # Create topic overlap analysis
    topic_overlap = {
        "Common Topics": common_topics,
        "Unique Topics": {}
    }
    
    # Find unique topics for each article
    for i, article in enumerate(articles):
        unique_topics = [topic for topic in article["Topics"] if topic_frequency[topic] == 1]
        topic_overlap["Unique Topics"][f"Article {i+1}"] = unique_topics
    
    # Generate final sentiment analysis
    final_sentiment = determine_overall_sentiment(sentiment_counts, articles)
    
    return {
        "Sentiment Distribution": sentiment_counts,
        "Coverage Differences": comparisons,
        "Topic Overlap": topic_overlap,
        "Final Sentiment Analysis": final_sentiment
    }

def generate_impact_statement(article1, article2):
    # Generate an impact statement based on article sentiments and topics
    if article1["Sentiment"] == "Positive" and article2["Sentiment"] == "Negative":
        return f"The positive news about {', '.join(article1['Topics'][:2])} is offset by concerns regarding {', '.join(article2['Topics'][:2])}."
    elif article1["Sentiment"] == "Negative" and article2["Sentiment"] == "Positive":
        return f"While there are concerns about {', '.join(article1['Topics'][:2])}, positive developments in {', '.join(article2['Topics'][:2])} may balance the overall impact."
    else:
        return f"The articles present different perspectives on {', '.join(set(article1['Topics'][:1] + article2['Topics'][:1]))}."

def determine_overall_sentiment(sentiment_counts, articles):
    # Determine overall sentiment based on distribution and article importance
    total = sum(sentiment_counts.values())
    
    if sentiment_counts["Positive"] > sentiment_counts["Negative"] + sentiment_counts["Neutral"]:
        return f"Coverage is predominantly positive. Positive news about {articles[0]['Topics'][0] if articles and articles[0]['Topics'] else 'the company'} is particularly noteworthy."
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"] + sentiment_counts["Neutral"]:
        return f"Coverage shows significant concerns, particularly regarding {articles[0]['Topics'][0] if articles and articles[0]['Topics'] else 'the company'}."
    elif sentiment_counts["Positive"] > sentiment_counts["Negative"]:
        return f"Coverage is cautiously positive, with some concerns noted about {articles[0]['Topics'][0] if articles and articles[0]['Topics'] else 'the company'}."
    elif sentiment_counts["Negative"] > sentiment_counts["Positive"]:
        return f"Coverage leans negative, though there are some positive developments in {articles[0]['Topics'][0] if articles and articles[0]['Topics'] else 'the company'}."
    else:
        return f"Coverage is mixed or neutral, with balanced perspectives on {articles[0]['Topics'][0] if articles and articles[0]['Topics'] else 'the company'}."

def process_news_articles(company_name, news_articles):
    processed_articles = []
    
    for article in news_articles:
        # Extract title - Now using the correct capitalized key 'Title'
        title = article.get("Title", "Untitled")
        
        # Extract summary
        summary = article.get("Summary", "No summary available")
        
        # Perform sentiment analysis
        sentiment = analyze_sentiment(summary)
        
        # Extract topics
        topics = extract_topics(summary)
        
        processed_article = {
            "Title": title,
            "Summary": summary,
            "Sentiment": sentiment,
            "Topics": topics
        }
        
        processed_articles.append(processed_article)
    
    # Perform comparative analysis
    comparative_analysis = perform_comparative_analysis(processed_articles)
    
    # Create final output
    output = {
        "Company": company_name,
        "Articles": processed_articles,
        "Comparative Sentiment Score": comparative_analysis,
        "Final Sentiment Analysis": comparative_analysis["Final Sentiment Analysis"]
    }
    
    return output