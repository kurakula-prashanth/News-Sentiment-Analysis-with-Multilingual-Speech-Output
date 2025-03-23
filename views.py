import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_news_data, generate_audio_summary

# Dictionary of language codes for audio summary generation
LANGUAGE_CODES = {
    "english": {"name": "English", "code": "en-US"},
    "hindi": {"name": "Hindi", "code": "hi"},
    "telugu": {"name": "Telugu", "code": "te"},
    "malayalam": {"name": "Malayalam", "code": "ml"},
    "tamil": {"name": "Tamil", "code": "ta"},
    "kannada": {"name": "Kannada", "code": "kn"}
}

def display_search_view(api_url, set_stage):
    """Display the search interface"""
    # Center column for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Search bar in a centered small container
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        company_name = st.text_input("Enter company name to analyze", 
                                    placeholder="e.g. Tesla, Apple, Microsoft",
                                    key="company_search")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Analyze button
        if st.button("Analyze News", use_container_width=True):
            if company_name:
                with st.spinner(f"Analyzing news for {company_name}..."):
                    success, result = fetch_news_data(api_url, company_name)
                    if success:
                        st.session_state.processed_data = result
                        set_stage("results")
                        st.rerun()
                    else:
                        st.error(result)
            else:
                st.warning("Please enter a company name")

def display_results_view(set_stage):
    """Display the results of the news analysis"""
    data = st.session_state.processed_data
    company_name = data["Company"]
    
    # Display company and summary
    st.markdown(f'<div class="sub-title">Analysis Results for {company_name}</div>', unsafe_allow_html=True)
    
    # Display sentiment distribution as both a pie chart and cards
    st.markdown('<div class="sub-title">Sentiment Distribution</div>', unsafe_allow_html=True)
    distribution = data["Comparative Sentiment Score"]["Sentiment Distribution"]
    
    # Create pie chart
    chart_col, cards_col = st.columns([1, 1])
    
    with chart_col:
        # Create pie chart using the sentiment data
        display_sentiment_chart(company_name, distribution)
    
    with cards_col:
        # Create sentiment count cards
        display_sentiment_cards(distribution)
    
    # Display overall sentiment
    st.markdown('<div class="sub-title">Overall Analysis</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <p style="font-size: 18px;">{data['Final Sentiment Analysis']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display common topics
    st.markdown('<div class="sub-title">Common Topics</div>', unsafe_allow_html=True)
    topic_overlap = data["Comparative Sentiment Score"]["Topic Overlap"]
    common_topics = topic_overlap["Common Topics"]
    
    if common_topics:
        st.markdown(f"""
        <div class="card">
            <p style="font-size: 18px;">{', '.join(common_topics)}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <p style="font-size: 18px;">No common topics found across articles</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display news articles
    st.markdown('<div class="sub-title">News Articles</div>', unsafe_allow_html=True)
    
    for i, article in enumerate(data["Articles"], 1):
        sentiment_class = f"card sentiment-{article['Sentiment'].lower()}"
        
        st.markdown(f"""
        <div class="{sentiment_class}">
            <h3>{article['Title']}</h3>
            <p>{article['Summary']}</p>
            <p>Sentiment: {article['Sentiment']}</p>
            <p>Topics: {', '.join(article['Topics'])}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Button to proceed to language selection
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Generate Audio Summary", use_container_width=True):
            set_stage("language")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Button to go back to search
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("New Search", use_container_width=True):
            set_stage("search")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def display_language_view(api_url, set_stage):
    """Display the language selection interface"""
    st.markdown('<div class="sub-title">Select Language for Audio Summary</div>', unsafe_allow_html=True)
    
    # Create language selection cards
    col1, col2 = st.columns(2)
    
    languages = list(LANGUAGE_CODES.values())
    
    with col1:
        for i in range(0, len(languages), 2):
            lang = languages[i]
            if st.button(f"{lang['name']}", key=f"lang_{i}", use_container_width=True):
                with st.spinner(f"Generating {lang['name']} audio summary..."):
                    success, result = generate_audio_summary(
                        api_url, 
                        st.session_state.processed_data, 
                        lang['code']
                    )
                    
                    if success:
                        st.session_state.audio_data = result
                        set_stage("audio")
                        st.rerun()
                    else:
                        st.error(result)
    
    with col2:
        for i in range(1, len(languages), 2):
            lang = languages[i]
            if st.button(f"{lang['name']}", key=f"lang_{i}", use_container_width=True):
                with st.spinner(f"Generating {lang['name']} audio summary..."):
                    success, result = generate_audio_summary(
                        api_url, 
                        st.session_state.processed_data, 
                        lang['code']
                    )
                    
                    if success:
                        st.session_state.audio_data = result
                        set_stage("audio")
                        st.rerun()
                    else:
                        st.error(result)
    
    # Button to go back to results
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Back to Results", use_container_width=True):
            set_stage("results")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def display_audio_view(set_stage):
    """Display the audio player and summary"""
    audio_data = st.session_state.audio_data
    
    st.markdown(f'<div class="sub-title">{audio_data["language_name"]} Audio Summary</div>', unsafe_allow_html=True)
    
    # Display the audio player
    st.markdown('<div class="card">', unsafe_allow_html=True)
    try:
        st.audio(audio_data["audio_file"], format="audio/mp3")
    except:
        st.warning("Audio file is not accessible directly. You may need to download it.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display the text summary
    st.markdown('<div class="sub-title">Summary Text</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <p style="white-space: pre-line;">{audio_data["summary_text"]}
    </div>
    """, unsafe_allow_html=True)
    
    # Buttons for navigation
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Back to Language Selection", use_container_width=True):
            set_stage("language")
            st.rerun()
    
    with col2:
        if st.button("Start New Search", use_container_width=True):
            set_stage("search")
            st.rerun()

def display_sentiment_chart(company_name, distribution):
    """Display a pie chart of sentiment distribution"""
    # Prepare data for pie chart
    sentiment_df = pd.DataFrame({
        'Sentiment': ['Positive', 'Negative', 'Neutral'],
        'Count': [distribution['Positive'], distribution['Negative'], distribution['Neutral']]
    })
    
    # Create a pie chart with custom colors
    fig = px.pie(
        sentiment_df, 
        names='Sentiment', 
        values='Count',
        color='Sentiment',
        color_discrete_map={
            'Positive': '#00cc00',
            'Negative': '#ff69b4',
            'Neutral': '#4682b4'
        },
        title=f'Sentiment Analysis for {company_name}'
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        margin=dict(t=40, b=40, l=40, r=40),
        legend_title_text='Sentiment',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

def display_sentiment_cards(distribution):
    """Display sentiment count cards"""
    # Create columns for sentiment counts
    pos_col, neg_col, neu_col = st.columns(3)
    with pos_col:
        st.markdown(f"""
        <div class="card sentiment-positive">
            <h3>Positive</h3>
            <h2>{distribution['Positive']}</h2>
        </div>
        """, unsafe_allow_html=True)
    with neg_col:
        st.markdown(f"""
        <div class="card sentiment-negative">
            <h3>Negative</h3>
            <h2>{distribution['Negative']}</h2>
        </div>
        """, unsafe_allow_html=True)
    with neu_col:
        st.markdown(f"""
        <div class="card sentiment-neutral">
            <h3>Neutral</h3>
            <h2>{distribution['Neutral']}</h2>
        </div>
        """, unsafe_allow_html=True)